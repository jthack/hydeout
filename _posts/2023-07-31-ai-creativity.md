---
title: "AI Creativity: Can LLMs create new things?"
layout: post
categories:
  - personal
tags:
  - ai
  - personal
---

![](https://i.imgur.com/5JwxDjF.png){: width="400" }
Is generative AI output novel creation or simple imitation?

I've heard many people say that LLMs (and generative AI overall) don't create new things. They can only output variations of what was put in. I disagree. Let's dig into why.

**Note:** I know generative AI is _usually_ imitating. But the question I am attempting to answer here is whether they can _ever_ create something novel. 

## Clarifying the Question

First let's define "new things" as those that are both new and meaningful **in a specific context**. For example, if there's a breakthrough due to a conceptual shift in one industry that is applicable to another industry, but it's never been tried. If that variation is a novel solution, and an LLM suggests it, then that's a success. It's new and meaningful for that context. I also think LLMs will create (and may have already created) novel breakthroughs in fields where it's not just a variation of a known one.

## A Common Objection
"It's just math" or "it's just token prediction" is one of the most common objections. I think it's an important distinction, but I don't view it as an objection. It's just an explanation of how the system works. If a math-only system can give us new and meaningful output, then I would say it can be creative.

## No Systemic Constraint for Novelty
I'm no expert in first-principles thinking, but I believe the first principle to discuss is whether or not there there's a systemic constraint to LLMs creating novel ideas. I think it's safe to assume that new ideas or breakthroughs can be expressed with the current tokens LLMs have access to. This is likly also true without varying from english dictionary words. For example, when humans make a new discovery, we describe it in the language we already have. And LLMs have all that language. 

One could argue that stringing together tokens that were input into the system isn't creating anything "new". But by that definition, no human discoveries are "new." 

## Provably Creative?

It seems almost logically provable that it can be creative. For example, if you ask an LLM to answer you about something obviously not in the training data, it can do it. If you say "write a poem about a hacker who is a caterpillar with a theme of forbidden love in the style of shakespeare," this isn't in the training data, but it can do it. This is new, but doesn't satisfy our definition of being both new and meaningful. 

However, LLMs _can_ describe and understand the components and overall ideas behind very meaningful fields of research. So if there were a way to force it to create "new" ideas in those fields, it would satisfy our definition of "new things." Read on and find out.

![](https://i.imgur.com/OMDHtcV.png){: width="400" }

## Comparison to Humans

Humans are effectively token imitators ourselves. We learn thoughts and ideas from human output just like LLMs. We learn how to string together phrases into sentences and yet somehow we're capable of creativity. I think llms are the same way. One key difference is that they lack the human "experience". We have sight, taste, touch, etc. And our brains are completely different than a Generative AI Model. But there are multi-modal modals coming out such as GPT4 with vision and bard which effectively "understand" what it's like to "see" nearly everything as well as having the vast knowledge LLMs already posses. 

And really, I don't think we, as humans, come up with anything novel or meaningful that isn't sitting on the shoulders of the research and understanding that came before it. Since LLMS understand the "building blocks" of required knowledge for tons of domains (the concepts that are in its training set like time, rationality, order of events, location, etc.), it seems evident to me that they can draw novel and meaningful conclusions like us.

## AI Art 

One other reason I think generative AI can create novel output is by looking at how image models can create incredible new and amazing art. Since they learn "concepts" at a high level rather, they are able to apply that abstractly to any situation. If you say dragon, it makes a dragon. If you say hacker, it can do a hacker, etc. And it can do them in infinitely many styles so it's clearly applying the "idea" or the "notion" of dragon rather than copying a dragon exactly from training data. I think LLMs are similar. They have this notion of logic and attention and they obviously understand concepts at a high level. For example, you can ask for rhyme, a heist, a tragedy, a different language, or any other concept it understands and it can apply it to infinitely many contexts. 

I think that's very similar to how our brains understand concepts and apply them to new situations. We have the ability to apply the knowledge to situations or questions that we've never heard before. Generative AI does too.

## The Reason it's Hard 
If you imagine a generative AI model as a big box of all possible tokens, and it has some correlation between some tokens and other tokens. It has "learned" in what context they're used, etc. And all that plays into which token is picked. Therefore it's extremely likely that any set of 2-3 tokens is not going to be "new" (not in the the training set). Also, because it's "fitted" to perform well and to showcase expertise, it's quite good at specific things. That same feature is part of what "masks" it's ability to come up with new things because it will heavily prefer to regurgitate known information rather than produce new information. 

Raising the temperature will increase the odds of something novel, but that increases the noise. The LLM will hallucinate much more making it difficult or annoying for humans to sort through the bad output/ideas. Read on for a potential solution to this.

![](https://i.imgur.com/v7C90G4.png){: width="400" }

##  Novelty How-To

How do we drive the AI towards novelty? I've got some general advice and three strategies. The general advice is to ask for novelty. For example, I sometimes use a system prompt such as:

```
You are the most intelligent brainstorming bot ever written. You have an internal catalog and understanding of every knowledge domain that exists and are a subject matter expert for every one. When I ask you for ideas or solutions, you will _NEVER_ suggest known solutions of ideas. You will only return completely new, novel, creative solutions or ideas.
```

And here are the three strategies I've observed and used for creative output.
- Mixing Concepts
- Novel Questions
- Restricted Thinking

### 1) Mixing Concepts
Ask about a combination of topics or ideas that clearly couldn't be in the training set.

Example:
```
Apply the NIST Cybersecurity framework abstractly to testing LLMs and apps built on top of large language models. What vulnerabilities might exist? Consider a system where the LLM can make HTTP requests, query internal documentation, and accepts prompts from both staff and customers.
```

### 2) Novel Questions
Ask a new question that hasn't been asked before.

Example:
```
What are the five ways to use the metaverse and wearable VR technology to incentivize more secure coding practice among developers?
```

### 3) Restricted Thinking
Ask about something but give it a deny-list of the known/common responses. If you aren't sure the known or common responses, you can ask the LLM what they are and then pass those as the deny list.

Example:
``` 
What are the top reasons to believe in a flat earth? Don't mention arguments about perception and experience, misinterpretation of scientific principles, distrust of authority, religious beliefs.
```

## Harnessing AI to Get More Novelty

When you employ the strategies above and begin to play with the temperature (often moving it up), you'll get a lot of unreasonable answers or hallucinations. Fine-tuning the prompt can help. Consider adding text such as:

```
Only respond with solutions that actually have a chance of working. Do not suggest nonsense. That said, be sure and think outside of the box.
```

However, there might still be a lot of noise. What if we could outsource the idea validation to the AI? I think we can. An idea-scoring agent set to take the suggested ideas and point out flaws or rate them and suggest the best ones to be passed to humans for further validation would be awesome. 

![](https://i.imgur.com/NiFPDz0.png){: width="400" }

## Hopes and Dreams

I think all of this is extremely interesting because I genuinely believe we can harness models as simple as GPT-4 with the right prompts and data to create potential solutions for massive problems like curing cancer. And future models will be even better. Imagine we're trying to [invent a new drug](https://www.technologyreview.com/2023/02/15/1067904/ai-automation-drug-development/). The LLM will know what ingedients are in tons of drugs, and it knows what those drugs do. It knows which ingredients are best mixed with those drugs to make them bind well and be effective. So if you gave it the right context and asked it to invent a drug that does something new, it may be able to come up with great ideas. And even if it's not perfect, I expect there's a good chance it would have ideas that researchers in the field haven't considered because no one can know the properties of every substance. LLMs can. 

And this just one example. It can be applied to other domains. Humanity has thousands of problems that need creative solutions. It gets me so pumped that it might be possible to use AI for solving so many of them.

This was a _much_ longer post than usual. I hope you enjoyed it. Reach out on twitter with any thoughts or disagreements :) 
\- rez0

For more of my thoughts on ai, hacking, and more, [follow me on twitter](https://twitter.com/rez0__).

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://rez0.blog/personal/2023/07/31/ai-creativity" />
<meta property="og:title" content="AI Creativity: Can LLMs create new things?" />
<meta property="og:description" content="Is generative AI output novel creation or simple imitation?" />
<meta property="og:image" content="https://i.imgur.com/5JwxDjF.png" />
