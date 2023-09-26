---
title: "Blog Evolution: The Journey Back to My Name"
layout: post
categories:
  - personal
tags:
  - hacking
  - personal
---

![](/assets/images/evolution.png){: width="400" }
_How and why I moved rez0.blog to josephthacker.com_

### The story of josephthacker.com
Back in college, I bought the domain josephthacker.com for something like 20 dollars. However, as a cash-strapped college student, I let it lapse at some point. 

When I wanted it back a few years later, I found out that a domain squatter was asking for a ridiculous 2,000 dollars. Needless to say, I didn't get it. Fast forward to last year, I managed to reclaim it for a few hundred dollars. 

Today, I am excited to announce the domain change from [rez0.blog](https://rez0.blog) to [josephthacker.com](https://josephthacker.com).

### Why change it?
I've been reading a fantastic book called "Key Person of Influence." This book has a lot of great ideas, and you should read it, but one of them rang true for my situation. It suggests making yourself easy to find online for your industry in order to increase opportunities. It got me thinking about how people might search for me. If they Google "Joseph Thacker," having my website under the same name will likely give it a better search ranking. Plus, it's pretty cool that my name includes the word "hacker."

With this change, and with Elon considering charging for twitter, I also thought it would be a good time to launch a newsletter so that people can find my content even if my twitter following goes away. 

Don't worry, I'm not starting another InfoSec newsletter. There are already some incredible ones out there. Instead, it will be an occasional email when I post something of high value on here. So I'd love it if you [subscribed to the newsletter](https://thacker.beehiiv.com/subscribe) so that I can let you know when that happens.


### How did I move it?
Most people might not care about this so feel free to skip it, but it was a pretty painless process so I wanted to share it. The best redirect for a permanent site move is 301. I didn't want to set up a server to do a 301 redirect. It turns out cloudflare has support for this. 

So, I attached josephthacker.com to cloudflare and set up a 301 redirect. Then you can use page rules to make the 301 config pass along the path so that old links still work.

This is what the page rules looks like:   
```   
URL
www.rez0.blog/*

Destination
https://josephthacker.com/$1
```   
```   
URL
rez0.blog/*

Destination
https://josephthacker.com/$1
```    

Thank you for reading :)  
\- rez0

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://rez0.blog/personal/2023/09/26/blog-evolution.html" />
<meta property="og:title" content="Blog Evolution: The Journey Back to My Name" />
<meta property="og:description" content="How and why I moved rez0.blog to josephthacker.com" />
<meta property="og:image" content="https://i.imgur.com/HVS5ESl.png" />
