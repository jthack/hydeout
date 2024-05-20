---
title: "Defining Real AI Risks"
layout: post
categories:
  - ai
tags:
  - cybersecurity
  - hacking
  - ai
---
![](/assets/images/robot_mech.png){: width="400" }
Yann LeCun is making the same mistake Marc Andreesen makes about AI risk. They aren't considering how powerful a system can be which incorporates generative AI with other code, tools, and features. LLMs can't cause massively bad outcomes, but it's not absurd to think human-directed LLM applications with powerful tools _could_ cause large-scale harm.

With the alignment team leaving OpenAI, lots of people are discussing the safety risks not being taken seriously internally at OpenAI. [Yann LeCun and others have basically made fun of these opinions, and even went so far as to consider it idiotic to worry about it](https://x.com/ylecun/status/1791890883425570823). I'm e/acc for the most part. I believe we should continue accelerating AI development and growth, but I think he's wrong to dismiss the risks out of hand. 

Marc Andreessen has a similar opinion about AI safety. It's crazy to me that this discussion lacks so much nuance when it's so important. So, I'll break down the real, practical categories of AI safety ([similar to how I did previously](/ai/2023/10/16/ai-security-terminology-issues.html)) but with concrete examples of bad outcomes so readers can actually consider the risks, decide what they think, and even think of solutions.

Before I get into it, I want to say that most of this can be boiled down to the fact that generative AI is basically a form of leverage. It gives more power to individuals and companies, but also it gives more power to bad actors who can get access.

### AI Alignment Risks

Some people are worried about a future AI system having goals that are in tension with human goals on such a scale that it wipes out millions or billions of people. I'd define this as an **AI alignment** concern. The attack scenario is something where the AI becomes conscious and wants to destroy all humans because we're bad or the well-known paperclip example where a system exhausts all resources in pursuit of some inane goal. But these simply don't seem plausible even in the next 10-15 years. 

However, if you consider that AI systems could be asked to harm specific groups of people such as Israel or Hamas utilizing AI in war against one another, you can see how alignment of AI systems is important. Also, I do think there is a non-zero chance of top researchers coming up with a self-learning breakthrough where a model significantly improves itself in a loop. In such a case, it's really hard to even guess what would occur. 

All that said, it's still seeming like we'll end up with open-source models of comparable strength to top closed-source models. And open source models can be trained to be uncensored or function without guardrails so, practically speaking, pushing for alignment might be a bit pointless because there will always be another model that isn't aligned well. If that's the case, there are some interesting implications about how to mitigate AI alignment risks. 

### AI Safety Risks

Safety is maybe the most ambiguous term in the industry, but I think there are some non-negligible risks worth considering that are safety-related and don't fall into alignment or security risks so I consider them **AI Safety** risks. Some of the risks below are critical enough to contribute to `p(doom)`, (the probability of very bad outcomes), but others are just worth mentioning to be comprehensive.

- Autonomous security testing: I call these [hackbots](https://josephthacker.com/ai/2024/02/21/hackbots.html). They are MUCH more than just LLMs, but LLMs enable and enhance them in a significant enough way that AI simulating human hacking was only possible in narrow niches and is now possible in a more abstract way that is actually interesting and can be used to find novel 0days on hardened bug bounty programs. Potential horrible outcome: other nations or terrorists get access to a hackbot or build their own, and it's talented enough to affect critical infrastructure or be deployed at a scale which causes a lot of chaos.
- AI usage in risky domains: This is the risk of generative AI being implemented in places where people's lives are on the line, like 911 dispatch, large-scale construction, engineering plans, military decisions, etc. I am actually optomistic that AI will have higher accuracy in many of these industries where humans already make mistakes, but it's noteworthy nonetheless. Lack of robust testing in these implementations could result in a prompt injection or hallucination leading to human deaths.
- Models lowering the barrier of entry for the creation of critical technology by bad actors. If simplified and descriptive how-to guides for destructive devices, dangerous biochemical substances, etc. are now available in almost any language, it's not _that_ different from what is possible today, but I think it's worth considering if we want to lower the difficulty of learning those things.
- Bias in models. These systems are extremely good at saving costs and automating processes, but humans are biased and therefore the models are too. It's extremely hard to remove that bias from models. So when models are implemented to cut costs, it's quite likely some discrimination and bias will occur. 

### AI Security Risks

- Prompt injection is an unsolved **AI Security** issue that has near-infinite variations of consequences depending on the design of the system. If it's a digital assistant, prompt injection might leak your emails or pictures, but in a weapons system, it could have more significant consequences.
- Invisible prompt injection will plague us for a long time due to the hard nature of fixing it and the fact it's an emergent ability. Invisible unicode tags must be filtered by every model provider OR they'll have to be filtered by every AI application.
- LLMs help phishing operations massively scale in terms of quality and personalization.

### Other AI Effects

- I have legitimate concerns about AI girlfriends contributing to the decline in families and children being born. I also worry that they'll be interesting, fun, and caring enough that they'll be many people's best (or only) friends. And I think that has a few positives, but lots of negatives.
- Deep fakes could make it hard for people to know what to trust. And it could make judges start to struggle with how much to weight photographic or audio proof of events. 
- Job displacement. Personally, I think job displacement just means the models are creating tons of utility and value, but I can see why some people are worried. I think we're clever enough to find a solution. It might UBI; It might be via other forms of job creation.

I want to iterate again that I am e/acc at heart, so I don't think we should pause or stop AI development, but I do think there are some legitimate concerns. And the complete disregard and belittling of people who are worried about the risks listed above is incorrect and unkind. 

Cheers! Hope you enjoyed the post :)

\- Joseph

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.
I also [post my thoughts on Twitter/X](https://x.com/rez0__).

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/ai/2024/05/18/defining-real-ai-risks.html" />
<meta property="og:title" content="Defining Real AI Risks" />
<meta property="og:description" content="Practical examples of AI risks" />
<meta property="og:image" content="https://josephthacker.com/assets/images/robot_mech.png" />
