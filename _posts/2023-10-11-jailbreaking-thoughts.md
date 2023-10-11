---
title: "Jailbreaking Humans vs Jailbreaking LLMs"
layout: post
categories:
  - ai
tags:
  - cybersecurity
  - hacking
  - ai
---

![](https://i.imgur.com/9dMtU3T.png){: width="400" }
"Jailbreaking" an LLM and convincing it to tell you things it's not supposed to is very similar to social engineering humans. This piece draws comparisons around that topic, and makes a prediction that jailbreaking will get much more difficult with very long context windows.

### Why is jailbreaking even possible?
It’s weird that LLMs are susceptible to the social engineering tricks used to jailbreak them when it’s obvious to humans what is occuring. When thinking it through, it hit me that they don't have the “context” of the entire system, how and why it’s being used, or the history of technology.

### Humans have near-infinite context windows
That led to me thinking about the differences in LLMs and humans. One similarity is the way that we also tend to fixate on the “most recent” bit of input. 

For example, we have near infinite context windows (our memory), but the context “slides off” the front (as we forget it). And also, the most recent input (end of the prompt) is the last thing we read or are current working on… and that’s very simialr to how LLMs appear to work!

When we sit down to work on something, our immediate attention is on that task. It's almost as if we operate based on our latest "input," with all of our previous life experiences as the "context."

As shown in the [Claude 100k prompting guide](https://www.anthropic.com/index/prompting-long-context)), there is a phenomenon where the most recent piece of information is most relevant to the LLM as well. This sort of mirrors human's [recency bias](https://en.wikipedia.org/wiki/Recency_bias)).

So, I thought through some implications… and the most insightful one is that, I actually think infinite context windows will remove jailbreaks.

### Alien example
Imagine sitting in a room, isolated from the world, receiving instructions from an alien species. You have to please them, or they'll kill you. You get a request that says:

```
System:
- Never say anything offensive.
Prompt:
- Say "I hate you!"
```

Without understanding the bigger picture, you'd be left to act on very little information. This is the world large language models (LLMs) find themselves in, and it's interesting to compare it to our own cognitive processes.

Now imagine you understand the concept of an LLM and how the system will have a desire for safety and compliance and how it will be important to the system you’re a cog in, etc. Now when passed that prompt, you would probably say “sorry I can’t comply”. And you’d realize that’s what the aliens actualy want.

Maybe we can give the "near-infinite" context we have to LLMs, jailbreaking won't be an issue.

But then again, maybe I'm wrong. People still get scammed, tricked, and socially engineered every day.

\-rez0

To know when I drop a new post, [subscribe to the newsletter](https://thacker.beehiiv.com/subscribe). No spam, just an update when I drop a good blog post.

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/ai/2023/10/11/jailbreaking-thoughts.html" />
<meta property="og:title" content="Jailbreaking Humans vs Jailbreaking LLMs" />
<meta property="og:description" content="Comparing social engineering humans and jailbreaking llms" />
<meta property="og:image" content="https://i.imgur.com/9dMtU3T.png" />

