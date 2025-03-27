---
title: "Simplify Interviews with guided-capture"
layout: post
categories:
  - ai
tags:
  - ai
  - productivity
---
![](/assets/images/guidedcapture_banner.png){: width="400" }
🎉 I just released my first Python package, [guided-capture](https://github.com/jthack/guided-capture), a cool new Python package that automates structured interviews using AI in order to gather the right context for your AI applications.

### Why guided-capture is Needed in the Current Market

A ton of AI features are limited by the knowledge in the minds of the end users and the application's ability to extract and use that knowledge. Whether your app is doing design work, conducting research, or simply trying to automate the user's request, the AI feature or agent will often struggle to perform at a high levelwithout the right context.

That's why I made guided-capture; in order to gather the right context for your AI use-cases.

### What Exactly is guided-capture?

`guided-capture` uses LLMs to help you conduct structured, goal-oriented interviews with users. It automatically generates relevant questions based on your objectives and neatly synthesizes responses into your desired output format. I think the best part is that it's completely UI-agnostic, meaning you can integrate it into any interface—CLI, web, mobile, you name it. And you can capture the answers in text, voice, or even a mix of both.

### Key Features You’ll Love

- **Goal-Oriented Interviewing**: Clearly define your topic and the output you want.
- **AI-Driven Questions**: Let the AI handle the heavy lifting of question generation.
- **Flexible Answer Collection**: Submit answers progressively or in bulk.
- **Intelligent Synthesis**: Automatically process responses into your preferred format.
- **State Management**: Easily save and resume your interview sessions.
- **Multiple LLM Support**: Compatible with various LLM providers like OpenAI and Anthropic.

### Getting Started Quickly

Installation is straightforward:

```bash
pip install guided-capture
```

Here's how easy it is to get started:

```python
from openai import OpenAI
from guided_capture import GuidedCapture

client = OpenAI(api_key="your-api-key")

capture = GuidedCapture(
    topic="Company Vision",
    output_format_description="A concise company mission statement",
    llm_client=client
)

questions = capture.get_questions()

# Just a sample way to snag user input. You can plug in any UI for answer capture.
for question in questions:
    print(f"\n{question}")
    answer = input("Your answer: ")
    capture.submit_answer(question, answer)

result = capture.process_answers()
print("\nFinal Output:", result)
```

### Integrate It Your Way

guided-capture’s UI-agnostic design means you can:

- Present questions via web forms, chat interfaces, or even voice inputs.
- Collect answers through text, voice, forms, or API calls.
- Control the interview flow and handle special cases with your own validations.

### Advanced Features for Power Users

- **Bulk Answer Submission**: Submit multiple answers simultaneously.
- **State Management**: Save and resume sessions effortlessly.
- **Custom Prompts**: Tailor the question generation and synthesis prompts to your specific needs.

Give it a try, submit a PR, and let me know if it's useful for your app. Happy hacking!

\- Joseph

P.S. The library is so simple that you don't really have to even use it, just ask AI to implmenent something similar. I just think it's a powerful paradigm that unlocks a bunch of new apps.

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.
I also [post my thoughts on Twitter/X](https://x.com/rez0__).

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/ai/2025/03/26/Simplify-Interviews-with-GuidedCapture.html" />
<meta property="og:title" content="Simplify Interviews with guided-capture" />
<meta property="og:description" content="Streamline structured interviews using guided-capture, an AI-powered Python package that simplifies question generation and response synthesis." />
<meta property="og:image" content="https://josephthacker.com/assets/images/guidedcapture_banner.png" />
