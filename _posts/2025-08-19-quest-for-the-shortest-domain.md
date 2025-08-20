---
title: "The Quest for the Shortest Domain"
layout: post
categories:
  - hacking
tags:
  - hacking
  - cybersecurity
---
![](/assets/images/domain_quest_banner.png){: width="400" }
In the world of bug bounty hunting, having a short domain for XSS payloads can be the difference in exploiting a bug or not... and it's just really cool to have a nice domain for payloads, LOL. 

One morning after I went full time bug bounty back in January, I decided to find me a nice domain for POCs and payloads. It turned into a full day journey. It was quite the adventure. I spent around **six hours** reversing domain-provider APIs and automating the process of finding them. I dove into the intricacies of ASCII and Unicode character counts, and the things I found were interesting.

### ASCII and Unicode

When it comes to domains for payloads, sometimes every character counts. ASCII and Unicode characters counts play a crucial role here. Many Unicode characters resolve to ASCII, which means if you're crafting an XSS or SSRF payload, a short domain can sometimes be your best friend. 

For example, a domain like `1.com` is straightforward with 4 ASCII and 4 Unicode characters because it doesn't condense. But then there's `rad.pw`, which I own . It has 5 ASCII characters but only 2 Unicode because "㎭" and "㎺" are each a single Unicode character.

### The Hunt for the Shortest Domain

My goal was to find the lowest character count possible, ideally 3 ASCII and 2 Unicode, like `1.rs`. Unfortunately, those are (mostly) all taken. So, I set my sights on finding a domain with 4 ASCII and 2 Unicode characters. 

However, finding such a domain at a reasonable price proved to also be a challenge. After much searching, I ended up with:  
- `rad.pw`: 5 ASCII, 2 Unicode, and "rad password" is a cool domain for POCs
- `t4.rs`: 4 ASCII, 3 Unicode because t4 doesn't condense, and short for [tars](https://interstellarfilm.fandom.com/wiki/TARS) the robot
- `km3.pw`: 5 ASCII, 2 Unicode. I got this one first, before finding the other two. If anyone is interested in having it, I don't really need it so let me know if you'd like it.

> **Sidenote**: Due to this whole process, I added this tool to my website: [ASCII to Unicode Character Reducer](https://josephthacker.com/unicode_reducer)

### Hidden Gems and Pricey Finds

During my search, I stumbled upon some intriguing domains. If you're willing to splurge, you can snag a 4 ASCII and 2 Unicode domain from [nic.st](https://nic.st/). Domains like `rs.st` are available, but they come with a hefty price tag—€799 due to being a 4-character domain, plus an annual fee of €29.

### The Holy Grail of Domains

The ultimate find though, and pricey at €1500 are a couple of domains: `2.st` and `9.st` (and maybe 1-2 other [number].st domains), are 3 ASCII and 2 Unicode. These are rare gems, and there's no way to reduce them further. 

Or is there?

All character counts I've mentioned so far include the period/dot, but technically, there's a set of Unicode character that combine a number and a period, like `⒉` so ones like these `⒉ﬆ` are actually even smaller. The sad thing is browsers (and unicode normalizers that I tested) don't convert ⒉ to `2.`, they just convert it to `2` and drop the period. So, while these domains are technically shorter, they don't work in practice AFAICT.

EDIT: Okay so I just found out that `⒉ﬆ` does get converted to `2.st` in javascript and python.

**JavaScript**:  
Both normalize('NFKC') and normalize('NFKD') convert "⒉ﬆ" → "2.st"  
**Python**:  
Both unicodedata.normalize('NFKC') and unicodedata.normalize('NFKD') ALSO convert "⒉ﬆ" → "2.st"

### Tell Me What You Find

I find all this super interesting so please tag me and tell me what your best domain is and if I've missed a tld or something with some golden domains.  
\- Joseph

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.
I also [post my thoughts on Twitter/X](https://x.com/rez0__).

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/hacking/2025/08/19/quest-for-the-shortest-domain.html" />
<meta property="og:title" content="The Quest for the Shortest Domain" />
<meta property="og:description" content="A journey into finding the most efficient domain for XSS payloads in bug bounty hunting." />
<meta property="og:image" content="https://josephthacker.com/assets/images/domain_quest_banner.png" />
