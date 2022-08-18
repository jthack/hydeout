---
title: "IDORs with unpredictable IDs are valid vulnerabilities"
layout: post
categories:
  - hacking
  - cybersecurity
tags:
  - hacking
  - cybersecurity
---

![](https://i.imgur.com/tpMrj6E.png){: width="300" }
*It's an eye-door, get it?*

There is an interesting debate around bug reports of IDORs with IDs which are not predictable. My stance is that they are valid vulnerabilities, they should be fixed, and this post will be a reference for why.

### What's an IDOR with an unpredictable ID?
If you're not sure what an IDOR is, [read Portswigger's post on it](https://portswigger.net/web-security/access-control/idor). If you know what an unpredictable ID is, you can skip to the next section.

If you're not sure what an IDOR with an unpredictable ID is, I'll tell you. First lets define an ID. In lots of applications, there will be a string of characters or numbers used to represent an object such as a user, organization, or a piece of data. The app makes requests to view or change the data for these objects _with_ that ID.

A predictable ID would be where the ID in those requests—and the corresponding backend database—is sequential (like  `467` for one object and `468` for another) or predictable (like if the username is being used as the ID).

So an "unpredictable ID" is anything used as an ID that isn't able to be predicted. It's most often a UUID, such as `0e925156-1dce-11ed-861d-0242ac120002`. But it could also be a concatenation of a random value and a unix timestamp or any other number of things.

### The debate
IDORs are a fairly common bug. They can be nearly any severity. For example, read-only IDORs to leak email addresses of other users might be a low. Read/write IDORs on user objects for other organizations would be a Critical on most programs.

This is the question we'll answer below: How should a report should be handled when there is an IDOR, but the ID required in the request is unpredictable?

Finding the bug and creating a POC isn't a problem for bug hunters or pentesters. They can use a second account to get the unpredictable ID for the first user to test the vulnerability. Here's the issue. A triager will often say "But how would the attacker get the ID?"

I'm glad you asked.

### The big list of unpredictable ID sources

Just because an ID is unpredictable, that doesn't mean it can't be found. Here's the many ways in which unpredictable IDs can be found.
- **Wayback machine**: Archives urls and pages. Unpredictable IDs are often in the parameters or in url path.
- **Alien vault OTX**: Threat intel which inadvertently archives urls as a part of its feature set. Unpredictable IDs are often in the parameters or in url path.
- **URLScan**: A website scanner for suspicious and malicious URLs. Companies submit data to it. This often contains unpreditable IDs in the parameters or paths.
- **Common Crawl**: Archives urls and pages. Unpredictable IDs are often in the parameters or in url path.
- **Google search**: Google indexes links which might have IDs in the path or parameters, caches pages which might have IDs on them, and indexes websites (like forums) where people often post urls or full requests which include IDs.
- **Github search**: Github public repos often include users posting their requests for debugging purposes in the Issues section, hardcoding unpredictable IDs into scripts, etc.
- **Insider threat - previous employee**: A previous employee who used the application on their personal laptop can look at the logs or local storage of their PC to get the IDs or they could have simply write them down before quitting or after getting fired but before access revocation.
* **Insider threat - RO user can view ID**: A current employee with read-only access in an app can often see the upredictable IDs. If there's an IDOR via unpredictable IDs, it's often a form of privilege escalation due to the fact that the IDOR represents a breach of trust already.
- **Referrer header**: Referrer headers with the ID in the path or GET parameters would leak the ID to other servers
- **Browser history**: Getting access to browser history via physical access or corporate handling of it would leak any IDs in the GET parameters or path
- **Web logs**: Anyone with http(s) logs would have access to any upredictable IDs in GET parameters or paths. This includes company IT, VPN providers, ISPs, etc.
- **Unknown or future bug ID leak**: Just because the report submitter does not have a current way to leak unpredictable IDs, it doesn't mean there's not a way. Or that there won't be a bug in the future that leaks those IDs.
* **It might not be unpredictable**: Any cryptography expert will tell you "random" with computers is very hard. It's one reason why [Cloudflare uses lava lamps](https://blog.cloudflare.com/randomness-101-lavarand-in-production/). Many "unpredictable" IDs may actually have a design flaw which leads to predictability.
* **Clickjacking to steal the ID**: Clickjacking can leak unpredictable IDs.

As you can see, there are countless way that an ID might be leaked.

![](https://i.imgur.com/wTp0WKS.png){: width="300" }
*Another eye-door :P*

### So how should it be handled?

If a program is using CVSS, it's an easy answer. The "Attack Complexity" metric should be raised to High because it's relatively complex to find an unpredictable ID. It's a perfect use of that metric. 

If a program doesn't use CVSS, I think it should be handled as a traditional IDOR and payed equivalently. However, if the company is confident there will never be ID leakage (such as the ID being in a POST request body, which would be less likely to leak in many of the above scenarios), accepting the report as a lower severity is another option. 

### Thanks
I appreciate you taking the time to read the blog. If you think this is useful, feel free to share it or even use it in a report as justification when receiving some push back.

If you have any questions or want to hear more from me, feel free to tweet/follow: [https://twitter.com/rez0\_\_](https://twitter.com/rez0__)

### Addendum: A curious critique
I've wanted to write this post for a long time. The straw that broke the camel's back was [this thread](https://twitter.com/Hishammir1/status/1559606917013639170?s=20&t=gyMDKpu2Zgu_UMNRl0wVWw). When starting to write it, I saw [Cosmin](https://twitter.com/inhibitor181)'s reply and immediately thought I might be wrong. Cosmin is one of the top hackers all-time. He's extremely talented. [This is the tweet](https://twitter.com/inhibitor181/status/1559749931056898048) that worried me:
> "It should really be N/A unless you have a way to grab UUID's. There are many apps that identify sessions or bearer tokens with UUID's. What do you do there? That is clearly not a bug and IDOR's that also need an UUID should fall under the no bug category, unless using UUID v1"

After thinking about it though, I realized the flaw in this line of thinking. IDORs with unpredictable IDs are different than session tokens or bearer tokens because sessions have timeouts and change on each login. A session token from a year ago popping up on the Wayback Machine doesn’t have impact. Also, same-org users can’t view each other’s session tokens, nor would that be a likely dev mistake in the future (leaking auth tokens to all users). But unpredictable IDs on objects in an app can be seen by all users of that organization, often leak in parameters or paths, show up in browset history, and are something other endpoints are prone to leaking.

### Bonus meme by [@hogarth45\_](https://twitter.com/Hogarth45_)
<blockquote class="imgur-embed-pub" lang="en" data-id="a/VrquUx6" data-context="false" ><a href="//imgur.com/a/VrquUx6"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>

Thanks again,

rez0

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://rez0.blog/hacking/2022/08/18/unpredictable-idors.html" />
<meta property="og:title" content="IDORs with unpredictable IDs are valid vulnerabilities" />
<meta property="og:description" content="A breakdown of why IDORs with unpredictable IDs are valid vulnerabilities." />
<meta property="og:image" content="https://i.imgur.com/tpMrj6E.png" />
