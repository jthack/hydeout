---
title: "Hacking with ChatGPT: Ideal Tasks and Use-Cases"
layout: post
categories:
  - hacking
tags:
  - hacking
  - cybersecurity
---

![](https://i.imgur.com/ciblWMD.png){: width="400" }
I've been using ChatGPT for lots of hacking or engineering tasks. It's extremely useful and much faster than executing on similar tasks without it. The key is knowing when to use it. Here's my thoughts on when to have it help and some awesome use-cases.

## The Ideal Tasks for ChatGPT

There are many ways in which ChatGPT is limited. It can help with almost anything, but I don't think it's an ideal tool for everything. 

Very small tasks for which there are existing tools are not the best use cases. If you need to encode some text, replace instances of one word with another, or get the answer to a well-known question, there are better tools for those things. If you're solving a really large problem such as restructuring an organization, it might make sense to ask ChatGPT for ideas, but it won't be able to solve such a large problem for you either. 

The sweet spot is when you need a task completed that is small or medium in size, would take more than a couple minues to do, but for which there isn't an existing good tool. And if it's not something ChatGPT can do directly, asking it to write a script to complete the task is a great way to still get a working solution. 

### Active Input Processing
The other unique skill of ChatGPT that people underestimate is the fact that it's actively processing the input. That's a super-power compared to googling. If you have an error in a bit of code, you might be able to very quickly google a solution to your issue. But you still have to _find_ that issue in the bit of code. ChatGPT is uniquely suited to be a massive advantage in those situations because you can paste your code into it as a part of the question.

Rather than "I'm getting error xyz, how do I solve this problem?", you can utilitze "Below is my code. I'm getting error xyz. Where is the problem and how do I solve it?". In short, it's more than a smart oracle. It's also a speedy assistant.

Let's jump into use-cases.

## ChatGPT Engineering Use-Cases

Now, let's talk about actual examples. These are the cool ways that I have used ChatGPT in the last few weeks:

**Write data-processing scripts.** 

As a hacker or security engineer, there is often data in a format that isn't ideal. Giving ChatGPT a plaintext description of a lengthy process and getting a working script as output just feels like magic. 

**Example prompt:**
```
Write a python script that reads the file "input.zip", unzips it, then reads the csv files inside line by line. It should take the second columns from the csv files, which are urls, and parse out the domain and save those in a new file called domains.txt. It should take the paths from the urls and save those in a file called paths.txt. 
```

**Make minified js code easier to read.** 

Often there is interesting minified javascript code in web applications that is useful for finding bugs. Parsing it and following what the functions do can be difficult. The files are often too large to paste the entire thing, but you can paste large parts of it into ChatGPT and ask it to comment the code while also making it more readable.

**Example prompt:**
```
Clean up the following js code by making it more readable and adding comments:

<js code here>
```

**Translate a json POST request into an x-www-form-urlencoded POST request.** 

As you probably know, json POST requests aren't vulnerable to CSRF. However, many frameworks and libraries allow urlencoded form POST bodies by default. So if there's not any CSRF protection on a json api request, trying url-encoded forms is a great way to find some bugs. The problem is that it's a lot of work to manually modify the request, especially if there are nested objects. This type of request will have ChatGPT doing it for you.

**Example prompt:**

```bash
Transform this entire burp request from json into a x-www-form-urlencoded request:

POST /api/files HTTP/2 
Host: test.com
Content-Length: 15
Content-Type: application/json

{"file":"rez0"}
```

**Coding error debugging**

This is what I was mentioning in the Ideal Tasks section. If you've got code that isn't working, is doing something weird, or is throwing an error. You can paste the relevant code into ChatGPT and have it help your find the problem (or just fix it for you!).

**Example prompt:**

```
Below is my code. I'm getting error "EXAMPLE ERROR". Explain the problem, fix my code, and put the output in a code block
```

### In conclusion

Hopefully I've given you some good ideas on how to use ChatGPT for security engineering and hacking. It's been a really good asset for me. Also, I'm sure other AI tools will pop up. This isn't unique to ChatGPT, it would probably all work nearly as well on GPT3. And it will likely all be way better on GPT4. 

Thanks for taking the time to read the post!

\- rez0

For more of my thoughts, bug bounty tips, and AI-generated hacker art, [follow me on twitter](https://twitter.com/rez0__). 

![](https://i.imgur.com/RaKHAae.png){: width="400" }

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://rez0.blog/hacking/2023/02/21/hacking-with-chatgpt.html" />
<meta property="og:title" content="Hacking With ChatGPT" />
<meta property="og:description" content="Ideal Tasks and Use-Cases" />
<meta property="og:image" content="https://i.imgur.com/ciblWMD.png" />
