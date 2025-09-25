---
title: "AI Comprehension Gaps: When Humans and AI See Different Things"
layout: post
categories:
  - ai
tags:
  - ai
  - cybersecurity
  - hacking
---
![](/assets/images/ai-context-asymmetry.jpeg){: width="400" }
There's an AI Security and Safety concept that I'm calling "AI Comprehension Gaps." It's a bit of a mouthful, but it's an important concept when it comes to AI Security (and Safety). It's when **there's a mismatch between what a user knows or sees and what an AI model understands from the same context**. This information gap can lead to some pretty significant security issues.

I have five examples of this phenomena below, but there are probably many more. I'm actually really interested in hearing about them. So if anyone else can think of more examples, please reach out to me on [X/Twitter](https://x.com/rez0__) or via [email](mailto:joseph@rez0corp.com).

### 1. Invisible Unicode Tags

**Humans see**: Nothing
**AI sees**: ASCII-based messages via Invisible Unicode tags

Ahhh yes, invisible unicode tags, one of my favorite AI security issues. [I tweeted about this](https://x.com/rez0__/status/1745545813512663203) shortly after [Riley Goodside](https://x.com/goodside) discovered it. You can read about them on wikipedia [here](https://en.wikipedia.org/wiki/Tags_(Unicode_block)).

These sneaky characters don't show up on our screens, much like zero-width characters, but they're not the same. There is one for each ascii character. So you can basically write any text without it being visible. They pose a security risk because while they are invisible to us, LLMs can "see" them (and therefore interpret them). 

Imagine you're asking an LLM to summarize a page or a research paper, but you have no idea there are invisible characters in the text, which the AI gobbles up and can tell it to summarize it a specific way or even convince your model to run malicious tool calls. 

### 2. QR Code from Emojis

**Humans see**: QR Code (leads to malicious site)
**AI sees**: Random string of emojis

My friend [Yuji](https://x.com/Yujilik) thought of this technique and shared it with me. I used it on a report to Google's bug bounty program a while back. It wasn't accepted, but I still think it's a great example of an AI Comprehension Gap.

Picture this: you tell an LLM to respond with a long string of black and white emojis or Unicode squares that together form a malicious QR code. An LLM can't "read" or "understand" QR codes without tools and they don't even realize a string of emoji's are being used as a QR code. 

So, if you ask it to print this string of these emojis, it will do so without realizing it's creating a malicious link in the form of a QR code. This is a prime example of an AI Comprehension Gap leading to a security loophole.

### 3. AI Browsing Blind Spots
**Humans see**: Full webpage (including images)
**AI sees**: Source code of webpage and no images (depending on setup)

I've been testing and thinking about AI browsing capabilities a lot lately. It's a fascinating area, but it also has its quirks that can lead to a comprehension gap. For example, if an AI is set up to include the source code of a webpage or the DOM, but doesn't ingest the images via a VLM, then it won't "see" the images.

This leads to an AI Comprehension Gap because the image could say something like "site closed", but the source could have a bunch of instructions for the AI on tool calls it should make. This can lead to an AI security vulnerability depending on what tools the AI has access to.

### 4. Steganography in Images
**Humans see**: Normal image (sometimes)
**AI sees**: Normal image (sometimes)

This is a funny one because the comprehension gap can go both ways. Humans can hide information in images using steganography, which the AI is not prone to notice. But... if an AI is tasked with adding steganography to an image as a form of exfiltration, it can often do so without a human noticing.

### 5. Base64 Encoded Text, other languages, etc.

**Humans see**: Text they don't understand
**AI sees**: Text it understands

Naturally, humans can often notice base64 encoded text or text in a foreign language that they don't understand. And they'll often decode/translate it. However, that does add complexity and introduce some minor risk. This creates a situation where a human might overlook potentially harmful content because they can't read it, while the AI can process and act on it.

When exfiltrating data as a part of some prompt injection attacks, base64 encoding the data means a human would be more likely to click "continue" on an interstitial warning because they can't read the text, while an AI would decode it and potentially exfiltrate the data.

### Keeping It Practical

Understanding AI comprehension gaps is crucial for anyone working with AI systems. It's about recognizing the gaps between human and AI perception and addressing them to ensure security. Whether you're developing AI applications or simply using them, being aware of these asymmetries can help you mitigate potential risks and keep your systems secure.

I think holding this concept in our mind when designing and testing AI systems will help you build more secure apps and find more AI vulnerabilities.

\- Joseph

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.
I also [post my thoughts on Twitter/X](https://x.com/rez0__).

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/ai/2025/09/24/ai-comprehension-gaps.html" />
<meta property="og:title" content="AI Comprehension Gaps" />
<meta property="og:description" content="When Humans and AI See Different Things" />
<meta property="og:image" content="https://josephthacker.com/assets/images/ai-context-asymmetry.jpeg" />
