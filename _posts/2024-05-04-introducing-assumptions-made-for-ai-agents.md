---
title: "assumptions_made"
layout: post
categories:
  - ai
tags:
  - ai
---
![](/assets/images/assumptions_made_standard.png){: width="400" }
_Introducing the `assumptions_made` field for AI Agents_

I've been thinking a lot lately about the current state of AI and large language models (LLMs). People are building really cool stuff with AI agents and chatbots that can call tools or use plugins, but there's clearly room for growth and innovation.

## The Challenge of Assumptions

One thing I've noticed is that these tools and plugins often use APIs. And whenever you have an AI agent or chatbot using an LLM to call an API, there are assumptions being made based on what the user says. 

Let me give you an example to show what I mean. Imagine I have an AI agent that I want to book a dinner date for me and my wife. I might say something like:

> "Make us dinner reservations at Malone's next Friday."

There are a few assumptions embedded in that request:

1. Which location of Malone's do I want? 
2. Am I bringing my kids?
3. What time do we typically eat dinner?

The LLM has to make a "best guess" based on the context it has, ask follow-up questsions, or refer to long term memory if I've clarified before. Different people will have different preferences for how many assumptions they're comfortable with the AI making.

## Introducing `assumptions_made`

So here's my idea: what if we create a mostly standardized metadata field called `assumptions_made`? This field would be populated by the LLM to list out the key assumptions it made when generating its response. Humans are almost always making assumptions. It makes sense that having it be a part of the way LLMs "work" would make them improve better.

Having an explicit list of assumptions could be really powerful. It would be possible to:

- Analyze the assumptions to see patterns and areas for improvement
- Give users control to tweak the assumptions 
- Eventually maybe bake it into the models themselves as a native feature

I think there's probably an optimal balance of assumptions we want LLMs to make to keep interactions low-effort but increase accuracy. 

![](/assets/images/ai_agents_assumptions_made.png){: width="400" }
## Benefits for Agent-to-Agent Communication

Where I think `assumptions_made` could be extra powerful is when we have AI agents communicating with each other. Imagine agent A makes a request to agent B. Along with its response to agent A, agent B also provides its `assumptions_made`. 

Now agent A has valuable extra context! It can see if agent B made any incorrect assumptions and provide clarification. Or it can determine that it needs more info from the user before proceeding.

Multi-agent systems haven't really hit production yet due to a variety of issues, but I believe something like this could be crucial for them to operate reliably. Without it, small incorrect assumptions can snowball and hurt consistency.

## Try It Out!

The great thing is we can start experimenting with this right now! If you're using ChatGPT, try this to get it to add a note to the long term memory:

```
Always include an "assumptions_made" field and value at the end of your responses where you list some assumptions you made in your response.
```

And if you're using custom apps built on LLM provider APIs, you can add the above to your system prompt.

Then start chatting and see what assumptions the LLM is making! I'd love to hear what you discover.

## Looking Ahead

In terms of implementation, `assumptions_made` could be a simple JSON field or just an addendum to the end of the LLM's output. The key is to have a standardized way to communicate assumptions. I'm excited to see where this idea goes! I think it has the potential to make AI agents much more robust and adaptable. 

Let me know your thoughts! Do you see value in an `assumptions_made` standard? How else could we improve communication between AI agents? 

\- Joseph

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.
I also [post my thoughts on Twitter/X](https://x.com/rez0__).

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/ai/2024/05/04/introducing-assumptions-made-for-ai-agents.html" />
<meta property="og:title" content="assumptions_made" />
<meta property="og:description" content="Proposing a new metadata field for AI agents to explicitly list the assumptions made during an interaction." />
<meta property="og:image" content="https://josephthacker.com/assets/images/assumptions_made_standard.png" />
