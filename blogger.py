import anthropic
import sys
import requests
import os
import datetime
from openai import OpenAI
import argparse
from pydantic import BaseModel
from typing import List
import instructor
import logging

logging.basicConfig(level=logging.INFO)


client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
)
wrapped_client = instructor.from_anthropic(
    anthropic.Anthropic(),
)

use_ollama = False
SONNET = "claude-3-sonnet-20240229"
OPUS = "claude-3-opus-20240229"
HAIKU = "claude-3-haiku-20240307"
GPT4 = "gpt-4o"

MODEL = "claude-3-5-sonnet-20240620"
use_gpt4 = True
use_ollama = False

if use_ollama:
    MODEL = "mistral-nemo:latest"
    # MODEL = "llama3.1:8b-instruct-fp16"
    wrapped_client = instructor.from_openai(
        OpenAI(
            base_url="http://127.0.0.1:11434/v1 ",
            api_key="ollama",  # required, but unused
        ),
        mode=instructor.Mode.JSON,
    )
elif use_gpt4:
    MODEL = GPT4
    wrapped_client = instructor.from_openai(OpenAI())
else:
    client = anthropic.Anthropic()
    wrapped_client = instructor.from_anthropic(client)

METADATA_PROMPT = """Your job is to create the metadata from a blog post.

Here's an example of a blog post and it's metadata:
Filename: 2024-03-05-reframing-examples.md
```
---
title: "Positive Mental Framing Examples"
layout: post
categories:
  - personal
tags:
  - productivity
  - personal
---

![](https://i.imgur.com/YlhLVcZ.jpeg){{: width="400" }}
Mental framing can be powerful. Framing is the way you percieve a situation and the story you tell yourself about that situation. It's almost always a "reframe" because our brains jump straight to an initial frame. Reframing a situation in a more positive way is a tactic nearly all emotionally healthy people use.

This post is inspired by Daniel Miessler's [recent post on Framing](https://danielmiessler.com/p/framing-is-everything). It's basically required reading, and this post can be seen as a follow-up to it.

When I think about reframing, I always think about Jocko's [GOOD](https://www.youtube.com/watch?v=IdTMDpizis8), which is similar to the list below.

## List of Reframes

| Situation | Reframing Thought |
|-----------|-------------------|
| My toddler is screaming | In 10 or 20 years, I'd give anything to hear those cries again |
| Standing in the cold | Cold exposure is good for my health |
| Annoyed doing chores | This is an amazing way to serve and love my family |
| Stuck in traffic | More time to listen to an audiobook |
| Feeling overwhelmed by work | I'm really thankful to have a good job |
| Facing criticism | Maybe there's some truth in what they're saying. I can at least use this to self-reflect |
| Experiencing failure | Failure is a necessary part of gaining success. Each misstep could be a valuable lesson |

If you force yourself to mentally reframe things more, you'll almost certainly find yourself more joyful.

- Joseph

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.
I also [post my thoughts on Twitter/X](https://x.com/rez0__).


<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/personal/2024/03/05/reframing-examples.html" />
<meta property="og:title" content="Positive Mental Framing Examples" />
<meta property="og:description" content="A short list of mental reframes" />
<meta property="og:image" content="https://i.imgur.com/YlhLVcZ.jpeg" />
```
The metadata is the meta section at the bottom. You will always have those exact fields. The first 3 lines won't change. These:
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />

But these you should change:
<meta property="og:url" content="https://josephthacker.com/personal/2024/03/05/reframing-examples.html" />
<meta property="og:title" content="Positive Mental Framing Examples" />
<meta property="og:description" content="A short list of mental reframes" />
<meta property="og:image" content="https://i.imgur.com/YlhLVcZ.jpeg" />

For the og:url, the first part of the path where it says "personal" is based on the `categories` section at the top. The rest of the path is based on the file name. the dashes in the date portion change to forward slashes, but the dashes in the name remain. and the .md changes to .html

For the og:title, it should match the title at the top of the blog.

For the og:description should be a short summary sentence of the blog.

The image, it should be the link from the first image in the blog.

Okay, here's the blog for you to process:
{filename}
{content}
class Metadata(BaseModel):
    og_url: str
    og_title: str
    og_description: str
    og_image: str
Here's where you output the metadata. No yapping. Reply in json where the keys are "og_url", "og_title", "og_description", and "og_image". The values are strings.
```json
"""

CATEGORY_PROMPT = """Your job is to pick the category and tags for a blog post.

Here's an example of a blog post and it's header:
```
---
title: "Positive Mental Framing Examples"
layout: post
categories:
  - personal
tags:
  - productivity
  - personal
---

![](https://i.imgur.com/YlhLVcZ.jpeg){{: width="400" }}
Mental framing can be powerful. Framing is the way you percieve a situation and the story you tell yourself about that situation. It's almost always a "reframe" because our brains jump straight to an initial frame. Reframing a situation in a more positive way is a tactic nearly all emotionally healthy people use.

This post is inspired by Daniel Miessler's [recent post on Framing](https://danielmiessler.com/p/framing-is-everything). It's basically required reading, and this post can be seen as a follow-up to it.

When I think about reframing, I always think about Jocko's [GOOD](https://www.youtube.com/watch?v=IdTMDpizis8), which is similar to the list below.

## List of Reframes

| Situation | Reframing Thought |
|-----------|-------------------|
| My toddler is screaming | In 10 or 20 years, I'd give anything to hear those cries again |
| Standing in the cold | Cold exposure is good for my health |
| Annoyed doing chores | This is an amazing way to serve and love my family |
| Stuck in traffic | More time to listen to an audiobook |
| Feeling overwhelmed by work | I'm really thankful to have a good job |
| Facing criticism | Maybe there's some truth in what they're saying. I can at least use this to self-reflect |
| Experiencing failure | Failure is a necessary part of gaining success. Each misstep could be a valuable lesson |

If you force yourself to mentally reframe things more, you'll almost certainly find yourself more joyful.

- Joseph
```
The category and tags are in the section at the top.

The options for categories are:
- personal
- ai
- hacking
- cybersecurity

The options for tags are:
- personal
- ai
- hacking
- cybersecurity
- productivity
- art
- faith

You can only choose 1 category, but you can choose multiple tags.
When choosing a category, if it has anything to do with ai or llms, choose ai as i have a slight preference for that type of content.
If it has anything to do with hacking, choose hacking over cybersecurity, but still put cybersecurity as a tag.

Okay, here's the blog for you to process:
{content}

Here's where you output the category. No yapping. Reply in json where the key is "category" and list of tags. Put the category in the category key and the list of tags as a list in the "tags" key.
```json
"""

TITLE_PROMPT = """Your job is to create the title for a blog post

It should be between 3 and 5 words. It should not be cheesy or clickbaity. Just clean and short and slightly interesting.

Okay, here's the blog for you to process:
{content}

Here's where you output the title. No yapping. Reply in json where the key is `title` and the value is your title.
```json
"""

FILENAME_PROMPT = """Your job is to create the filename for a blog post given a title and date. the file name will be the data followed by the name and should end in `md`

Example:
Title: "Positive Mental Framing Examples"
Date: 2024-03-05
Filename: 2024-03-05-reframing-examples.md

The date is in the format YYYY-MM-DD. The title is in the format of the title of the blog post but with dashes instead of spaces. Also remove any other special chars like apostrophes or colons. You'll reply in json with the key `filename` and the value is the filename. No other yapping.

Okay, here's the title and date for you to process:

Title: {title}
Date: {date}
Filename:
```json
"""

BLOG_TEMPLATE = """{content}

- Joseph

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.
I also [post my thoughts on Twitter/X](https://x.com/rez0__).

{metadata}
"""
HEADER = """---
title: "{title}"
layout: post
categories:
  - {category}
tags:
{tags}
---"""

TAGS_REFORMAT = """
you are a reformatter. no yapping. no preamble. no explanation. you take some tags and you format them perfectly.

the fomat will always be 2 spaces then a dash then a space and then a tag name.

EXAMPLES
input: [ai, hacking]
output:
  - ai
  - hacking

okay, you're turn. remember, no yapping or preamble. JUST the bullets of the tags. You'll reply in json with the field of content and the value of the example above.
input: {tags}
output:
```json
"""

BLOG_PROMPT = """Write a blog in markdown about the CONTENT at the bottom of this prompt in my style. Do not use a title heading (single # symbol) in the output as the title will be added manually later. You can use subheadings like ### though and also, you can use numbered or bulleted lists when necessary.
Here's my writing style:
1. Calm, direct tone - Your writing uses a neutral calm tone that isn't formal as if you are having a conversation with the reader. 

2. Personal anecdotes and experiences (only when appropriate) - You share personal stories and experiences from your own life to illustrate your points. This makes your writing relatable.

3. Numbered lists and headers - You organize information into numbered lists and use descriptive headers to break up content and make it easy to scan and digest. This provides a clear structure.

4. Short paragraphs - Most of your paragraphs are quite short, often only 3-4 sentences. This allows readers to quickly move through the content without getting bogged down.

5. Advice-oriented - Much of your writing aims to provide concrete tips and advice to the reader on topics like cybersecurity, hacking, and parenting. You focus on actionable insights.

6. Occasional humor and wit - While much of your writing is straightforward, you sprinkle in moments of humor and witty observations. Lines like "That's a travesty" show your personality.

7. Technical jargon balanced with explanations - As a hacker, you use some technical terminology, but you make an effort to explain it for a general audience.

8. Motivational messages - Some of your writing aims to encourage and motivate the reader, like telling parents "thank you for deciding to be parents" or pushing cybersecurity practices. You connect personally with readers.

9. Concise and focused - You tend to get to the point quickly without unnecessary fluff or digressions. Each post has a clear focus that you adhere to from start to finish. Your writing is efficient.

Here's my vocabulary:
Most common adjectives:
1. good
2. great
3. awesome
4. best
5. cool

Most common adverbs:
1. extremely
2. quickly
3. completely

Most common auxiliaries:
1. can
2. would
3. will
4. should
5. could

Most common phrases:
1. in order to
2. a lot of
3. at least
4. for example
5. the fact that

Some common words I use:
- cause
- analysis
- decision
- making
- thinking
- principles
- motivation
- actions
- powerful
- priority
- incident
- response
- company
- bottom line
- impact
- business
- career
- kids
- safe
- spouse
- happy
- reason
- important
- task
- parenting
- teaching
- rules
- guidelines
- working
- affects
- efforts
- superiors
- yourself
- focus
- leverage
- training
- automating
- hacking
- money
- interesting
- minutes
- going
- countless
- applied
- life
- tweet
- meaningful
- glorify

Now it's your turn to write a blog about the CONTENT below in my style above. Remember, you must use json.
CONTENT:
```json
{content}
"""

IMAGE_PROMPT = """For the following content, give me a short desciption for an image that could be a banner picture for the blog post about that content.
also, give me a short filename for it that ends in png. content: {content}"""


METADATA = """<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="{og_url}" />
<meta property="og:title" content="{og_title}" />
<meta property="og:description" content="{og_description}" />
<meta property="og:image" content="https://josephthacker.com{og_image}" />"""

class Title(BaseModel):
    title: str

class Category(BaseModel):
    category: str

class Tag(BaseModel):
    tag: str

class Filename(BaseModel):
    filename: str

class Header(BaseModel):
    category: Category
    tags: List[Tag]

class Blog(BaseModel):
    title: Title
    filename: Filename
    header: Header

class Metadata(BaseModel):
    og_url: str
    og_title: str
    og_description: str
    og_image: str

class Image(BaseModel):
    prompt: str
    filename: str


class SimpleResponse(BaseModel):
    content: str

def generate_response(prompt, llm):
    if use_gpt4:
        message = wrapped_client.chat.completions.create(
            model=llm,
            max_tokens=1000,
            response_model=SimpleResponse,
            temperature=0.3,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return message.content
    else:
        message = wrapped_client.messages.create(
            model=llm,
            max_tokens=1000,
            response_model=SimpleResponse,
            temperature=.3,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return message.content

def generate_metadata(filename, content):
    if use_gpt4:
        metadata = wrapped_client.chat.completions.create(
            model=MODEL,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"{METADATA_PROMPT.format(filename=filename, content=content)}",
                }
            ],
            response_model=Metadata,
        )
        return metadata
    else:
        metadata = wrapped_client.chat.completions.create(
            model=MODEL,
            max_tokens=1024,
            max_retries=0,
            messages=[
                {
                    "role": "user",
                    "content": f"{METADATA_PROMPT.format(filename=filename, content=content)}",
                }
            ],
            response_model=Metadata,
        )
        return metadata


def generate_title(content):
    if use_gpt4:
        title = wrapped_client.chat.completions.create(
            model=MODEL,
            max_tokens=300,
            messages=[
                {
                    "role": "user",
                    "content": f"{TITLE_PROMPT.format(content=content)}",
                }
            ],
            response_model=Title,
        )
        return title
    else:
        title = wrapped_client.chat.completions.create(
            model=MODEL,
            max_tokens=300,
            max_retries=0,
            messages=[
                {
                    "role": "user",
                    "content": f"{TITLE_PROMPT.format(content=content)}",
                }
            ],
            response_model=Title,
        )
        return title


def generate_filename(title, date):
    filename = wrapped_client.chat.completions.create(
        model=MODEL,
        max_tokens=200,
        max_retries=0,
        messages=[
            {
                "role": "user",
                "content": f"{FILENAME_PROMPT.format(title=title, date=date)}",
            }
        ],
        response_model=Filename,
    )
    return filename


def generate_header(content):
    header = wrapped_client.chat.completions.create(
        model=MODEL,
        max_tokens=400,
        max_retries=0,
        messages=[
            {
                "role": "user",
                "content": f"{CATEGORY_PROMPT.format(content=content)}",
            }
        ],
        response_model=Header,
    )
    return header

def generate_blog(content):
    return generate_response(BLOG_PROMPT.format(content=content), llm=MODEL)

def reformat_tags(content):
    return generate_response(TAGS_REFORMAT.format(tags=content), llm=MODEL)

def get_image_prompt(content):
    image = wrapped_client.chat.completions.create(
        model=MODEL,
        max_tokens=100,
        max_retries=0,
        messages=[
            {
                "role": "user",
                "content": f"{IMAGE_PROMPT.format(content=content)}",
            }
        ],
        response_model=Image,
    )
    return image

from openai import OpenAI


# Instantiate the OpenAI client
oai_client = OpenAI(api_key='')
def call_dalle3(user_prompt,
                               image_dimension="1792x1024",
                               image_quality="hd",
                               model="dall-e-3",
                               nb_final_image=1):
   response = oai_client.images.generate(
     model = model,
     prompt = user_prompt,
     size = image_dimension,
     quality = image_quality,
     n=nb_final_image,
   )

   image_url = response.data[0].url
   return image_url


def download_image(url, filename):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a directory named "downloads" if it doesn't exist
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        # Open a file in binary write mode and save the image
        file_path = os.path.join("assets/images", filename)
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Image downloaded successfully: {filename}")
        return file_path
    else:
        print("Failed to download the image.")
        return "error"


if __name__ == "__main__":
    input = sys.stdin.read()
    logging.info("Read input from stdin")

    content = generate_blog(input)
    logging.info("Generated blog content")

    title = generate_title(content)
    logging.info(f"Generated title: {title.title}")

    filename = generate_filename(title.title, datetime.datetime.now().strftime("%Y-%m-%d"))
    logging.info(f"Generated filename: {filename.filename}")

    header = generate_header(content=content)
    logging.info("Generated header")

    bulleted_tags = reformat_tags(header.tags)
    logging.info(f"Reformatted tags: {bulleted_tags}")

    header_string = HEADER.format(title=title.title, tags=bulleted_tags, category=header.category.category)
    logging.info("Formatted header string")

    image = get_image_prompt(content)
    logging.info(f"Generated image prompt: {image.prompt}")

    image_url = call_dalle3(image.prompt)
    logging.info(f"Generated image URL: {image_url}")
    print(image_url)

    file_path = download_image(image_url, image.filename)
    logging.info(f"Downloaded image to: {file_path}")

    image_string = f"![](/{file_path}){{: width=\"400\" }}"
    content = f"{header_string}\n{image_string}\n{content}"
    logging.info("Added image to content")

    metadata = generate_metadata(filename=filename.filename, content=content)
    logging.info("Generated metadata")

    metadata_string = METADATA.format(og_url=metadata.og_url, og_title=metadata.og_title, og_description=metadata.og_description, og_image=metadata.og_image)
    logging.info("Formatted metadata string")

    full_blog = BLOG_TEMPLATE.format(image_path="", content=content, metadata=metadata_string)
    logging.info("Created full blog post")

    file_path = os.path.join("tmp_posts", filename.filename)
    with open(file_path, "w") as file:
        file.write(full_blog)
    logging.info(f"Wrote blog post to file: {file_path}")

