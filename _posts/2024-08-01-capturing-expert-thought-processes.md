---
title: "Internal Monologue Capture"
layout: post
categories:
  - ai
tags:
  - ai
  - hacking
  - cybersecurity
  - productivity
---
![](/assets/images/expert-monologue-ai-banner.png){: width="400" }
I can't stop thinking about a new concept AI applications could benefit from. I'm calling it **internal monologue capture**. When Daniel Miessler and I were hanging out a few months ago, I had told him a huge thing that AI applications need is the **internal monologue** from experts. I'm pumped to finally write a blog about it.

### Examples and explanation
Here's the best way to explain it. Imagine if an AI hacking system had the internal monologue of the best XSS exploiter when attempting to exploit XSS. We can literally _give it_ that if you have that expert write down their thoughts as they exploit an XSS. 

As an example, I'm pretty decent at content discovery via fuzzing. When I'm looking at fuzzing results,  my brain is constantly streaming with thoughts. It usually looks something like this: 'That path looks interesting because of xyz, I should try x. If that returns a 301, then I know xyz is true and then I should try abc.' It's a constant monologue of thoughts and potential actions.

But it's not just hackers that do this. This internal chatter happens for nearly anyone. Take copy editors, for example. They're thinking stuff like 'That sounds a little too cheesy, let's change this word' or 'That's too formal. I'll rephrase it to say...'. The better a person is at a task, the higher quality this internal monologue will be. These little nuggets of expertise are perfect for prompting an AI model to do that same task. And this type of content isn't captured very well in the space of training data.

AI can already doing a pretty good job at many tasks, but imagine if we could feed it the thought process of many human experts. I belive it would simultaneously enable some use-cases that AI can't do or is really bad at, and would make current capabilities improve significantly.

### Implementation and next steps
So, two things:

1. We need to create a way to capture the internal monologue of experts. It's basically tapping into their brains and extracting task-specific wisdom.

2. Then we use that data to increase the quality of current AI applications. I'm mostly thinking about in-context learning via system prompts or examples, but it may be possible to even fine-tune models to become absolute pros at specific tasks with enough internal monologue.

Initially, for many products, this capture can just be asking internal staff with expertise to write down their internal monologue when performing their tasks. Eventually, I think this would make an amazing product.

So yeah, who's going to build an internal monologue capture app?

\- Joseph

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.
I also [post my thoughts on Twitter/X](https://x.com/rez0__).

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/ai/2024/08/01/internal-monologue-capture.html" />
<meta property="og:title" content="Internal Monologue Capute" />
<meta property="og:description" content="Using human experts' internal monologue to improve AI applications." />
<meta property="og:image" content="https://josephthacker.com/assets/images/expert-monologue-ai-banner.png" />
