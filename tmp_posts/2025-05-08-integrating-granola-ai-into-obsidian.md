---
title: "Integrating Granola AI into Obsidian"
layout: post
categories:
  - hacking
tags:
  - hacking
  - cybersecurity
  - ai
---
![](/assets/images/ai_crossroads.png){: width="400" }
### Reverse Engineering Granola AI: A Journey into Obsidian Integration

#### The Challenge

Granola AI had become my go-to for jotting down quick thoughts and ideas. However, I wanted to integrate these notes into Obsidian, my primary note-taking app. The problem? There wasn't a straightforward way to do this. So, I decided to reverse engineer the Granola AI app to find the right API endpoints. This wasn't just a technical challenge; it was a puzzle waiting to be solved.

#### Proxying the System

The first step was to proxy my system. By doing this, I could monitor the network traffic between the Granola AI app and its servers. It's like eavesdropping on a conversation, but with packets of data. This method allowed me to identify the API endpoints that were being used by the app. It's a bit like being a detective, piecing together clues to solve a mystery.

#### Discovering the Supabase.json

While digging through the data, I stumbled upon a file named `supabase.json` on my disk. This file contained the credentials needed to access the Granola AI's backend. It was like finding a key to a locked door. With these credentials, I could pull the notes directly into Obsidian.

#### The Python Script

To automate the process, I wrote a Python script that utilized the discovered API endpoints and credentials. This script seamlessly transferred my notes from Granola AI to Obsidian, making my workflow more efficient and integrated. 

[personal anecdote about writing the Python script here]

#### Final Thoughts

This experience was a reminder of the power of curiosity and technical skills. By leveraging reverse engineering, I was able to create a solution that worked for me. It's a testament to the fact that sometimes, the best tools are the ones you build yourself. 

If you're interested in the technical details, feel free to reach out. And remember, the journey of hacking and integrating tools is as rewarding as the destination itself. 

Stay curious, keep hacking, and never settle for less than awesome solutions.

- Joseph

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.
I also [post my thoughts on Twitter/X](https://x.com/rez0__).

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/hacking/2025/05/08/integrating-granola-ai-into-obsidian.html" />
<meta property="og:title" content="Integrating Granola AI into Obsidian" />
<meta property="og:description" content="Exploring how to integrate Granola AI notes into Obsidian through reverse engineering." />
<meta property="og:image" content="https://josephthacker.comhttps://josephthacker.com/assets/images/ai_crossroads.png" />
