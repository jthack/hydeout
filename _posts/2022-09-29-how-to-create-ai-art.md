---
title: "How to get setup to create awesome AI art"
layout: post
categories:
  - art
tags:
  - art
  - personal
---

![](https://i.imgur.com/4yAgZMY.jpg){: width="300" }
Generating Hacker art via AI has been a passion of mine for a few months. I was accepted into Dalle 2's Beta pretty early. I learned how it worked and to optimize my creations. 

Midjourney was around at that time, and I hopped over to try it out. It's what I primarily use these days due to the unlimited generations for $30. I've kept up with the AI art scene. I often get asked how to generate AI art. This is a guide I hope will be useful to all those people.

*Note: The AI art stuff is changing really fast. New models and new features are added all the time. If any of this is incorrect, feel free to ping me on twitter, but no promises on keeping it up to date.*

## DALL·E 2

The instructions here are simple. Go to [here](https://labs.openai.com/signup) to get started. There's no longer a waitlist. Now you can start generating images.

### Pricing
- You get 50 free credits your first month.
- 15 free credits will replenish every month after that, on the same day of the month.
- $15 for 115 more credits

### Tips
DALL-E is really good at interpreting user input. It is very literal in its interpretation. So if you want it to "look cool", you need to give it descriptions that would make it look cool.

Some of my favorites are:
- `key anime visual of <concept>`
- `professional digital art`
- `still from a pixar movie`
- `overlook concept art fantasy landscape`
- `cinematic lighting`

And you can combine them. So a great prompt would be:

`key anime visual of a warrior angel wearing a glowing hoodie typing on a laptop, professional digital art, trending on artstation, background is a cyberpunk city`

Voila! 🎉 You should get an image similar to this:
![](https://i.imgur.com/PKs6XHr.png){: width="300" }

## Features
DALL-E has some really nice features:
- Uploading pictures you want to edit or generate around
- In-painting where you can remove aspects you don't like and regenerate them
- Out-painting where you can create conglomerates by creating around an image
- A variations button. I don't have much luck with it though. It never changes enough.

![](https://i.imgur.com/Ni5rB4Q.png){: width="300" }

One big downside is that it's output (assuming you're not outpainting) is 1048x1048 pixels.

## Midjourney

Go to [https://www.midjourney.com/home/](https://www.midjourney.com/home/) and choose "sign-up". This will have you login with discord. If you don't have discord, sign up for it. Then browse to [the docs here](https://midjourney.gitbook.io/docs/#create-your-first-image) and follow those instructions. I prefer to create images without being in the cluttered Discord channels made by Midjourney. So I recommend clicking on the bot and "messaging" the prompt to it. Then all future generations can be done via direct messages.

![](https://i.imgur.com/Nfj8E8D.png){: width="300" }

### Pricing
- You get a bit of free machine time. So just play with it until you run out.
- $10/month for 200 minutes of machine time per month (it goes pretty far)
- $30/month for unlimited slow generations (called relax mode)
- $600/year for enterprises

### Tips
Midjourney is less good at interpreting user input by default. They are always releasing new models and flags to use. Midjourney is less literal in its interpretation. So if you want it to "look cool", you don't always have to give it qualifiers. That said, using descriptions can make it look much better.

Some of my favorites are:
- `8k detailed`
- `sci fi poster`
- `cyberpunk style`
- `synthwave style`
- `drawn by artgerm`

And you can combine them. So a great prompt might be:

`a hacker cat typing on a laptop, as drawn by artgerm, synthwave style, 8k --testp`

Notice the `--testp`  in my prompt. This is because (at the time of writing) has multiple "models" you can invoke. The default engine (without using `--testp` or `--test`) has a really cool artsy vibe without adding extra descriptors. But it has a lot of issues with smaller details. The new models are much better at details but have a bit less of an artsy vibe without good descriptions. Personally, I think `--testp` is way better. I always use it.

Voila! 🎉 You should get an image similar to this:
![](https://i.imgur.com/cCtVl09.png){: width="300" }

### Features
Midjourney has a different set of awesome features. Since they take flags like a command line program, there's too much to explain here. I'll cover a few and link you to their documenation so you can learn them.
- Uploading pictures as "inspiration" and weighting the new generation to them
- The ability to generate a different aspect ratios
- Faster shipping of updates
- Variations as a feature built in that is quite good. It changes just enough to be useful
- Documentation is here [https://midjourney.gitbook.io/docs/](https://midjourney.gitbook.io/docs/)

## Stable Diffusion

Stable diffusion is probably the biggest impact player right now. It was actually incorporated into Midjourney's test and testp models which is what makes them so good. SD is free and open-source. There are lots of guides to getting set up on it. The quality depends on your machine and how long you let it spend generating images. I personally have not gotten set up on it other than using a simple jupyter notebook on Google collab. Here's some guides on how to get set up if you decide to try it:

- https://www.assemblyai.com/blog/how-to-run-stable-diffusion-locally-to-generate-images/
- https://stealthoptional.com/tech/how-to-run-stable-diffusion/
- https://medium.com/geekculture/run-stable-diffusion-in-your-local-computer-heres-a-step-by-step-guide-af128397d424

One thing that is amazing about stable diffusion is all the ways you can customize it if you're a developer. It's being added to photoshop plugins, people are helping it learn a "concept" and use it across generations, it's being incorporated into other tools, etc.

## Thanks
I appreciate you taking the time to read the post. Hopefully you enjoyed it. I post a lot of my art on [my twitter](https://twitter.com/rez0__/media). If you click the media tab, you can scroll back through the art I've posted. Also, I sell some of the best generations as NFTs here: https://opensea.io/collection/hackers-by-rez0. Even if you're not interested in buying, it's a cool place to see some of the best images.

rez0


<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://rez0.blog/art/2022/09/29/how-to-create-ai-art.html" />
<meta property="og:title" content="AI art" />
<meta property="og:description" content="How to get setup to create awesome AI art" />
<meta property="og:image" content="https://i.imgur.com/4yAgZMY.jpg" />
