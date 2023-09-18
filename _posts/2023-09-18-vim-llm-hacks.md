---
title: "vim + llm = 🔥"
layout: post
categories:
  - hacking
tags:
  - hacking
  - personal
---

![](https://i.imgur.com/C6uGNdw.png){: width="450"}
If you don't use vi/vim, you might not find this post that practical, but it also might convince you to try it!

## Leveraging vim's Visual Mode

For those unfamiliar, vim has a feature calle 'visual mode'. This allows you to select some text, which can then be manipulated in various ways. One such way is hitting the colon key, followed by an exclamation point. This allows you to run a shell command using the selected text as input from stdin. Then the output from the command is written directly into the file, replacing the selected text right before your eyes. Here's a simple sort example.

<video width="700" controls>
  <source src="/assets/vimvisualexample.mov" type="video/mp4">
  Your browser does not support the video tag.
</video>
*Using llm to sort lines in vim*


## Applying llm to this feature

This might sound complex, but it's not too bad (and super useful). When combined with the capabilities of an LLM, it becomes a superpower.

Imagine, for instance, that you've written a piece of text with some typos in it. Rather than having to manually go through and correct each one, you could simply select the text in vim, run a command using an LLM, and have all of the errors automatically corrected.

Or perhaps you've written a piece of code, but forgot to add comments explaining what it does. Again, you could select the code in vim, run a command using an LLM, and have comments automatically generated and inserted into your code.

You could even use an LLM to help finish a sentence or paragraph that you're struggling with live inside your text editor. Simply select the text you've written so far, run a command using an LLM, and have the rest of the sentence or paragraph automatically generated for you. Naturally with all of these, there is a bit of latency for the calls to the llm.

<video width="700" controls>
    <source src="/assets/vimcomment.mov" type="video/mp4">
    Your browser does not support the video tag.
</video>
*Using llm to comment some code*

<video width="700" controls>
    <source src="/assets/vimfinish.mov" type="video/mp4">
    Your browser does not support the video tag.
</video>
*Using llm to finish a paragraph*

## Caveats

There are a few caveats. Vim doesn't load .bashrc/.zshrc or .bash_profile/.zsh_profile for its command execution. It _does_ however, load the env file. So you will need to put your functions in `.zshenv`. 

You will also have to install the command line tool `llm` by Simon Willison if you don't have it. Here is a link to the github repo: https://github.com/simonw/llm/

Also, llms don't always reflect the entire input into the response (and they may include some preamble about their response) so your llm calls will need to account for that. To make it easy to understand and replicate, I've put my `.zshenv` functions below. Simple add these to your `.zshenv` and they'll start working in vim:

```bash
comment(){
  llm -s 'Add comments to this code. Respond with the code and comments. Do not alter the functional aspect of the code, but still return it. Be sure and include the code in the response. Do not respond in a markdown code block. Just respond with the code and comments. Do not preamble or say anything before or after the code. for example: If the user sent "print(1)\nprint(2)", you would reply "# Prints 1\nprint(1)\n# Prints 2\nprint(2)"' - o temperature .2
}
```
```bash
fix(){
  llm -s 'Fix the syntax of this code. Respond with the code including any fixes. Do not alter the functional aspect of the code, but simply fix it and respond with all of it. Do not respond in a markdown code block. Just respond with the code. Do not preamble or say anything before or after the code. for example: If the user sent "print(1", you would simply reply "print(1)"' -o temperature .2
}
```
```bash
edit(){
  llm -s 'Edit this text to remove unnecessary filler words such as "like", "you know", and unimportant adverbs. Respond with the edited text only. Do not alter the speaking style or primary content.' -o temperature .1
}
```
```bash
blog(){
  llm -s 'Write a blog about the topic from the user as a wise and succinct writer such as Paul Graham or Tyler Cowen, but only use high school term paper vocabulary or lower.' -o temperature .4 -o presence_penalty .2 -m  gpt-4
}
```
```bash
finish(){
  message=`cat`
  echo -n $message
  echo -n $message | llm -s 'Finish this input. Respond with only the completion text. Do not respond with the input. Do not preamble or say anything before or after the completion. For example: If the user sent "The sky  is", you would simply reply " blue." If the input is code, write quality code that is syntactically correct. If the input is text, respond as a wise, succinct writer such as Paul Graham or Tyler Cowen, but only use high   school term paper vocabulary or lower.' -o temperature .4 -o presence_penalty .2 -m gpt-4
}
```

## Peace

I really hope you enjoyed these tips. If you're a vim and llm user (or willing to try them), I think it will really open your mind up to what is possible with these tools!

\- rez0

For more of my thoughts on hacking and other stuff, [follow me on twitter](https://twitter.com/rez0__). 

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://rez0.blog/personal/2023/09/18/vim-llm-hacks.html" />
<meta property="og:title" content="vim + llm = 🔥" />
<meta property="og:description" content="Using vim's visual mode with the llm tool for fun and profit" />
<meta property="og:image" content="https://i.imgur.com/C6uGNdw.png" />
