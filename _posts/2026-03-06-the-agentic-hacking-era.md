---
title: "The Agentic Hacking Era: Ramblings and a Tool"
layout: post
categories:
  - hacking
tags:
  - ai
  - hacking
  - cybersecurity
---
![agentic_hacking_era_banner.png](/assets/images/agentic_hacking_era_banner.png){: width="400" }
A few weeks ago I wrote about [how AI is going to impact bug bounty](https://josephthacker.com/ai/2026/02/24/ai-s-impact-on-bug-bounty.html). That post was mostly predictions. This one is about what's actually happening right now.

First off, that prediction is already coming true. Since that post, there's been an explosion of people posting about their bugs found with claude code on X. 

I've been using AI coding agents (specifically Claude Code) as my primary hacking companion for a couple months. Not as a side-thing, but as my main way to hack. And the results have been stupid good. I'll post a Q1 update soon that details it all. I personally think that the biggest reason it's now possible is that Anthropic's 4.6 models made a huge leap in their understanding of hacking. 

### One Big Component

Most people building AI hackbots (including me, initially) have their agents making raw curl requests or writing custom scripts. It works, but it's messy. Reproducing what the agent did is painful. Validating findings means asking the agent or grepping through logs instead of being able to look at the request and response side by side.

I wrote a [guest post on the Caido blog](https://caido.io/blog/2026-03-06-caido-skill) about a new skill I helped build that connects AI agents directly to Caido's SDK. The TLDR: your agent can now programmatically create replay sessions, manage findings, pull auth tokens, search request history, and do everything you'd normally do by clicking around in the proxy UI. And it all happens through the same Caido instance you already use.

The real win is human-in-the-loop without any extra effort. Your agent runs, finds stuff, creates replay sessions with descriptive names. You open Caido and it's all right there. Same interface you already know. You can verify, edit the replay tabs as well, dig deeper, etc. There's no extra context switching between your agent's output and your tool that youre used to.

As I mentioned in the Caido post, using this setup, I've found 15 vulnerabilities in the last 6 weeks. Most of them High or Critical severity.

### Two Main Arguments

The biggest two buckets of thought on this topic online are:
- Anyone can do it, even your grandma
- There's no way AI is coming for pentesters/bug hunters jobs

So let me address each of those. First, I do think it's easy to forget all the stored knowledge that top-tier talent has. We've seen hundreds or thousands of bugs and not-bugs, so it's really easy for me to dismiss or triage bugs when Claude says "JACKPOT! THIS IS CRITICAL!". And it's often not. For this reason, Grandma can't do it. And pointing Claude code at the right target/scope/endpoints for high ROI also requires decent taste. THAT SAID, the economics for how cheap tokens are under Claude Max subscriptions and the value of even Low bugs in bug bounty, I actually do think it's possible for beginners to make money for the next couple months by jumping on this train.

The second group of thoughts around pentester/hunter impact is really interesting. I think human-in-the-loop is going to be big for at least a couple years. That's why the Caido skill is so great. It loads up traffic, requests, and findings right into the tool you're already using. Also, if you don't think this will impact your job, please please please just do three things for me:
1. Tell Claude Code (Opus) to make some bughunting/pentesting skills to use
2. Point it at some scope
3. Watch it work

If you're a skeptic, I think it will surprise you.

### What this means

I said it in my last post and I'll say it again: people using AI agents are going to capture the majority of bug bounty market this year. The low-hanging fruit will get more sparse. The attack surface coverage will be broader. Hunters who adapt will do well. Hunters who don't will have a rough time.

For pentesters and red teamers, the same logic applies. More ground covered, more thorough testing, and you still maintain the careful human oversight that clients expect.

### Get started

If you're not using coding agents for hacking yet, start now. If you want to try the Caido skill, check out the [Caido skill](https://github.com/caido/skills). It's open source and it works with models as small as Haiku.

And if you want to hear me and other hunters talk about this stuff every week, we cover it on [Critical Thinking Bug Bounty Podcast](https://ctbb.show).

\- Joseph

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.
I also [post my thoughts on Twitter/X](https://x.com/rez0__).

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/hacking/2026/03/06/the-agentic-hacking-era.html" />
<meta property="og:title" content="The Agentic Hacking Era" />
<meta property="og:description" content="How AI coding agents changed my bug bounty workflow and why proper tooling like Caido integration matters." />
<meta property="og:image" content="https://josephthacker.com/assets/images/agentic_hacking_era_banner.png" />
