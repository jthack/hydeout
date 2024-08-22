---
title: "The Data Wall, Agents, and Planning-Based Evals"
layout: post
categories:
  - ai
tags:
  - ai
---
![](/assets/images/ai_crossroads.jpeg){: width="400" }
I've been thinking a lot about the whole "data wall" thing with LLMs lately. It's the idea that LLMs can't or won't improve because we've exhausted all the possible training data. I don't buy it. The best models are appearing to plateau, but it's not a lack of training data.

The real issue? We're asking them a ton of questions that have clear-cut, correct answers. Think about it - if you ask an LLM what 2 + 2 is, and it says 4, how can you improve on that? You can't.   

It boils down to one idea: **You can't improve upon truth.** 

### The Illusion of Plateauing

So here's what's happening:

1. Most state-of-the-art models are nailing the answers to a lot of common questions.
2. These questions often have objectively true answers.
3. When all the top models are getting these right, it's hard to see improvement, and they're just jockying for first place based on what output format humans like best.

It's not a data wall we're hitting - it's just that squeezing out extra gains when they're all correct so often is tough. 

### The Next Frontier: Agentic and Action-Based Improvements

Now, here's where things get interesting. Like many others, I think the next big leap is going to be in agentic and action-based improvements. We need to set up better evals for that kind of stuff though.

Take the [LMSYS leaderboard](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard), for example. It's cool and all, but it's mostly judging what a human finds as a good or bad response. That's a start, but we need to go further.

### The Need for Planning-Based Evals

In my work as an AI engineer, and in most complex AI projects I see shared on X, there's a notion of a "planner." What we really need is a planning-based eval. Here's what I'm thinking for a planning-based eval:

1. All "questions" should be actually be tasks.
2. Humans judge the LLM's ability to create a proper plan.
3. This plan should take into account the LLM's set of tools or resources (either given as a part of the prompt OR let it make up what tools it would require).

This kind of eval would give us a much better idea of how these models can actually help in real-world applications. It's not just about spitting out facts anymore - it's about using that knowledge to create actionable plans.

So yeah, I don't think LLM development is hitting a wall. We're just at the point where we need to change how we're measuring progress. And that's pretty exciting if you ask me. The future of AI is all about action and planning, not just regurgitating facts. I can't wait to see where this goes, and I'm super thankful I get to be here to experience it!

\- Joseph

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.
I also [post my thoughts on Twitter/X](https://x.com/rez0__).

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/ai/2024/08/22/data-wall-agents-planning-based-evals.html" />
<meta property="og:title" content="The Data Wall, Agents, and Planning-based Evals" />
<meta property="og:description" content="My thoughts on the data wall and how we're moving from factual knowledge to action-based planning and evaluation." />
<meta property="og:image" content="https://josephthacker.com/assets/images/ai_crossroads.png" />
