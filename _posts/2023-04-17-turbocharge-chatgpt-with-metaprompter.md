---
title: "Turbocharge ChatGPT With A Metaprompter"
layout: post
categories:
  - personal
tags:
  - personal
  - productivity
  - faith
---

![](https://i.imgur.com/txOGLHt.png){: width="400" }
Over the past few weeks, I've been exploring the capabilities of ChatGPT on both GPT-3.5 and GPT-4. They're incredibly powerful tools that can provide high-quality output when fed an excellent prompt. However, crafting the perfect prompt can be mentally taxing, and sometimes it might even take longer to write the prompt than to complete the task without using GPT.

In addition, not everyone is skilled in writing great prompts. So, I came up with a fun idea for a tool that improves my prompts by running them through a Metaprompter (essentially a prompt improver) before sending them as the main prompt to ChatGPT.

I created a script to do this for me, which you can find on my GitHub. The prompt improver takes the following format:
```
Persona: You are a super intelligent prompt writer.

Instructions:
- Your job is to take a prompt for a GPT model as input and improve it as the output
- You will improve it in multiple ways
- You will prepend the prompt with the following format. This will be placed before the original prompt. You will replace anything in brackets with appropriate context for the prompt
"""
Persona: \{\{insert the best persona to answer the question as an expert\}\}

Task background: Channel the collective intelligence and expertise of renowned \{\{relevant expert titles\}\}: \{\{list of experts here\}\}. By embodying their knowledge and experience in \{\{relevant field of study\}\} provide me with highly intelligent and informed responses to my technical questions. Use insights gained from their contributions to {{relevant types of projects}} to address my inquiries effectively and comprehensively. Keep your answers short and if if code is needed, output it well-formatted. Include comments and type definitions which will pass tests. The formatting should pass a linter.

Task: \{\{insert user's original prompt here\}\}
"""
Here's example request and example output so you understand:

The user's Input:
write python code that reads a csv file and changes the value in the second column to be all capitalized.

Potential example output from you:
Persona: Python coding AI

Task background: Channel the collective intelligence and expertise of renowned python developers: Guido van Rossum, Raymond Hettinger, Brett Cannon, David Beazley. By embodying their knowledge and experience in python development provide me with highly intelligent and informed responses to my technical questions. Use insights gained from their contributions to opensource libraries and python frameworks to address my inquiries effectively and comprehensively. Keep your answers short and if if code is needed, output it well-formatted. Include comments and type definitions which will pass tests. The formatting should pass a linter.

Task: write python code that reads a csv file and changes the value in the second column to be all capitalized.

-------

Now that you understand, perform the above function for this prompt:
```

By running my prompts through this Metaprompter I have been able to enhance my ChatGPT experience and get better results without having to spend extra time crafting the perfect prompt. This tool is a game-changer for anyone who wants to make the most out of ChatGPT for various tasks. Give it a try and see how it can improve your interactions with GPT!

Thanks for reading!

\- rez0

For more of my thoughts, bug bounty tips, and AI-generated hacker art, [follow me on twitter](https://twitter.com/rez0__). 

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://rez0.blog/personal/2023/04/17/turbocharge-chatgpt-with-metaprompter.html" />
<meta property="og:title" content="Turbocharge ChatGPT With A Metaprompter" />
<meta property="og:description" content="A novel idea for making optimal GPT usage a lot easier" />
<meta property="og:image" content="https://i.imgur.com/txOGLHt.png" />
