import anthropic
import sys
import os
import base64
import logging
from openai import OpenAI
import instructor
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)

# Initialize OpenAI client
oai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Initialize Claude client
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
wrapped_client = instructor.from_anthropic(client)

class Image(BaseModel):
    prompt: str
    filename: str

IMAGE_PROMPT = """For the following content, give me a short desciption for an image that could be a banner picture for the blog post about that content. I like my images to be black and white. Respond with json where the values are prompt for the image_prompt and filename for name that i will save the image as. be sure the filename ends in png. content: {content}"""

def get_image_prompt(content):
    image = wrapped_client.chat.completions.create(
        model="claude-3-sonnet-20240229",
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

def call_dalle3(user_prompt,
               image_dimension="1536x1024",
               image_quality="high",
               model="gpt-image-1",
               nb_final_image=1):
    response = oai_client.images.generate(
        model=model,
        prompt=user_prompt,
        size=image_dimension,
        quality=image_quality,
        n=nb_final_image,
    )
    image_base64 = response.data[0].b64_json
    return image_base64

def generate_image(content):
    # Create assets/images directory if it doesn't exist
    os.makedirs("assets/images", exist_ok=True)
    
    # Get image prompt and generate image
    image = get_image_prompt(content)
    image_base64 = call_dalle3(image.prompt)
    
    # Save the image
    file_path = "assets/images/" + image.filename
    with open(file_path, "wb") as f:
        f.write(base64.b64decode(image_base64))
    logging.info(f"Saved image to: {file_path}")
    
    return file_path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        content = sys.argv[1]
    else:
        content = sys.stdin.read()
    
    file_path = generate_image(content)
    print(file_path)  # Print the path so it can be captured by other scripts 