---
title: "How to prevent Forced Browsing"
layout: post
categories:
  - cybersecurity
tags:
  - cybersecurity
  - hacking
---

![](https://i.imgur.com/eQaB5XZ.png){: width="300" }
*Eliminate an entire vulnerability class from your web server in less than an hour*

As a hacker and bug hunter, one of my favorite bugs to find is information disclosure via [forced browsing](https://owasp.org/www-community/attacks/Forced_browsing). This is when you can find sensitive data (such as credentials or secret keys) in a file not referenced by the application. The most common way these vulnerabilities are found is by using content discovery tools like fuzzers.

## The risks

Information disclosure by forced browsing occurs for a variety of reasons. I've found entire webroots in zip files, exposed git folders, and authentication bypasses.

Perhaps a zip of the webroot was created to save as a backup. A copy may have been left on the server. This is a big deal since many servers run php or asp code, which is executed server side. The credentials in those files normally can't be accessed via the browser because it is executed server-side before being sent to the browser. However, downloading them as a zip means all the files can be read.

Git folders are often left behind because deploying servers or features by simply cloning the repo is quite easy. With these on a webserver, unless there is a config which blocks access to this folder, it's now exposed to the internet.

One final example would be when there is authentication which is not enforced on all endpoints. By browsing directly to endpoints without an authentication check, unintended access can be achieved.

![](https://i.imgur.com/VyAFApu.jpeg){: width="300" }

## The fix in theory

I want to explain the fix at a high level first because many organizations will have their own way to implement this process. Also, any non-technical readers can have a clean break at the end of this section and still have a practical step-by-step requirement to pass to their security team.

Here's the overview of how to drastically reduce exposures on your webservers. This will be performed for each server:
1. Gather all paths to all content on the web server (where the website resides)
2. Make requests from an external perspective (simulating a normal visitor) for each of those paths. This will likely be done via code or a tool.
3. Go through the output to determine if any of the exposed files or paths are sensitive and should not be exposed to the internet.
4. Remove any exposed files or folders. Add authentication to any pages which were lacking it.

If your website has a login process that is for customers or external users, this same process would be performed from an authenticated perspective as well.

## The fix in practice

Some practicalities that make the above theory a little more difficult to apply at scale are:
1. There might be a lack of knowledge on how to output all the files in a useable format
2. Browsing to hundreds of files is time-consuming
3. Files are added and modified on the server all the time

So here are the solutions:

1. To list all files in a nice format (in bash/zsh), change to the webroot directory of your server and run this command to save all file paths to `all_files.txt`:
```bash
find . -name "*" -print | cut -d/ -f2- > all_files.txt
```

2. Now we will use that list to fuzz the web server for those files. I prefer [ffuf](https://github.com/ffuf/ffuf) for this task but you feroxbuster, dirsearch, dirb, and others will also work:
```bash
ffuf -c -u https://example.com/FUZZ -w all_files.txt -t 5 -mc 200 -ac -o output.csv -H "User-agent: Mozilla/5.0 Security Testing"
```

Since this post is geared towards defensive security folks and ffuf is more of an offensive tool, I'll break down the command.

`-c`  is just colorized output, which is nice.
`-u`  is for the input url. The FUZZ keyword is what will be replaced by the liens in the wordlist for each request.
`-w`  is for wordlist
`-t`  is for the number of threads to use. By default, ffuf is relatively fast using 40 threads. Toning that down will help reduce the likelihood of getting blocked by the WAF.
`-mc 200`  match all 200 response codes. "Match" here meaning display it on the output and put it in the output file.
`-ac`  tells ffuf to "autocalibrate". Some servers respond with a 200 that says "not found" rather than a 404. Also, other websites just show the main page if you pass a path that doesn't exist. Autocalibrate tests the server with paths that shouldn't exist, builds a baseline, and doesn't show or save those results.
`-o`  outputs to the following filename.
`-H`  is for any header. We are using it to set a custom user agent for traffic tagging, as well as making sure we aren't using the default ffuf agent in case it's blocked by the WAF.

3. We can continuously monitor new files, fuzz for them, and alert developers or engineers with a simple script. I've put an example script below with in-line notes explaining each command. It's fully plug and play if you follow the instructions. Setup should only take a few minutes. This can be set to run regularly via crontab. I also put it in a gist:

https://gist.github.com/jthack/ba2c5a1061a913a5c698b9e2b152a362

```bash
# Before the first run, read the comments and change the script for your company
# Before anything, install ffuf with `go install github.com/ffuf/ffuf@latest`
# Before anything, install anew with `go install -v github.com/tomnomnom/anew@latest`

# Change the WEBROOT variable below to the location of the webroot
WEBROOT=/var/www/html/CHANGE/ME
# This changes to the webroot directory
cd $WEBROOT
# This makes a directory for storing the files used for this script. Change it to be whatever path you want.
PROJPATH=/home/changeme/project
mkdir -p $PROJPATH
# This finds all the files and writes their paths to the file
find . -name "*" -print | cut -d/ -f2- > $PROJPATH/all_files.txt
# Change to projpath director
cd $PROJPATH
# This fuzzes for all the files and matches 200 response code and saves output in the file. You can use ffuf's other nice outputs if desired but it will break the rest of the script.
ffuf -c -u https://example.com/FUZZ -w all_files.txt -mc 200 -ac -o output.csv
# The first run of this will put all exposed paths into the file. After that, only newly exposed files will be output.
cat output.csv | cut -d, -f2 | anew all_exposed_paths.txt
# You can now review all_exposed_paths.txt or output.csv or to make sure nothing is exposed that shouldn't be. Due to the way "anew" works, this will only show you the new paths each time it is ran.

# Alternatively (what I recommend) is to pipe the output of the previous command into a slack or discord hook. If you do that, comment out the last line and use this one. As mentioned before, due to anew, you will only be pinged/alerted when there is a NEW 200 response path.
# cat output.csv | cut -d, -f2 | anew all_exposed_paths.txt | to_slack

# Here's my tool I use to send messages to slack (it's only 3 lines of code): https://github.com/jthack/toslack
```

Your company will be significantly more secure if you regularly scan and review all the servers you own with a script like the one above.

## Follow up with me
If you're a security engineer who does this and finds some sensitive stuff exposed, I would LOVE to hear about how this helped. Please [tweet or dm me](https://twitter.com/rez0\_\_) the story!

If you're a company who doesn't fully understand this post, feel free to reach out with any questions!

If you're a company with a bug bounty program and want to outsource the reviewing-of-the-output aspect, do the first step and send me a list of all the paths! I'll review it and report anything sensitive to your bug bounty program!

## Caveats
This strategy may not work for:
- Domains which point at something third party like a SaaS product (unless you're using an on-prem version).
- Sites which get "built" before deploying like jekyll does. Many of the resource paths are dynamically built at run-time before deployment so simply listing files and directories won't get all the paths needed. It's definitely still worth doing though as you'll catch some things.
- Large-scale companies with hundreds or thousands of domains might find this process difficult. That said, focusing on your core domains would be a great place to start, and the provided script could be pushed via salt/other tools to automate it at scale.


## Thanks
I really hope you enjoyed this article. I'd appreciate it if you shared the post with anyone you thinkg would find it useful.
\- rez0



<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://rez0.blog/cybersecurity/2022/09/22/prevent-info-disclosures.html" />
<meta property="og:title" content="How to prevent Forced Browsing" />
<meta property="og:description" content="Eliminate an entire vulnerability class from your web server in less than an hour" />
<meta property="og:image" content="https://i.imgur.com/eQaB5XZ.png" />
