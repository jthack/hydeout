---
title: "Rabbit r1: Innovative Device, Security Concerns"
layout: post
categories:
  - cybersecurity
tags:
  - cybersecurity
  - hacking
  - ai
---
![](/assets/images/rabbit-r1-security-concerns.png){: width="400" }
Hey friends, let me start by saying - I'm actually really excited about Rabbit's new r1 device. The idea of having an AI assistant and image analyzer in a portable little "Pokedex" is extremely cool. And being able to connect it to services like Midjourney for AI art generation and Spotify for music? Awesome!

But here's the thing that has me a bit concerned. Instead of using a nice secure method like OAuth to link accounts, the r1 has you log into services through VNC in their portal.

Don't get me wrong, I love the convenience of being able to connect applications to an AI device. But having it snapshot your credentials or session data is... not great from a security standpoint. 

Here's why:

1. You're effectively logging into someone else's computer (the VNC machine) with your account info so Rabbit's staff could potentially access and abuse your credentials or account data to those accounts
2. If there's a keylogger on those VNC machines, they could also harvest login details for accounts you access through login-with-Google/Facebook/etc. 
3. If an attacker got cross-user access to the VNC machines or if they aren't properly encrypting the creds, it's 1 entry point to then access _everyone's_ accounts.

Maybe I'm just being paranoid, but giving a third-party that level of access seems really risky to me. Especially when OAuth and other secure auth methods exist.

Now I'm not saying Rabbit has bad intentions here. I think they needed to get the product out the door. And some services don't offer service accounts, API keys, or Oauth grants. But this VNC login setup introduces some serious potential vulnerabilities that concern me.

If you're still intending to use the service, be cautious about what accounts/services you connect through the VNC portal and consider setting up a second account for this specific use-case.

Honestly, this whole ordeal is exactly why [I think we really need innovation in the auth industry for AI agents](/ai/2024/02/05/secure-ai-agents.html).

What are your thoughts? Am I being too cynical here or do you share the same security concerns? 
Let me know by [hitting me up on X/Twitter](https://x.com/rez0__).

\- Joseph

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.  

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/cybersecurity/2024/04/26/rabbit-r1-innovative-device-security-concerns.html" />
<meta property="og:title" content="Rabbit's New r1 Device: Cool Tech, But Is It Secure?" />
<meta property="og:description" content="A blog post exploring the potential security risks of Rabbit's new r1 device and its reliance on a VNC remote desktop portal for account authentication." />
<meta property="og:image" content="https://josephthacker.com/assets/images/rabbit-r1-security-concerns.png" />
