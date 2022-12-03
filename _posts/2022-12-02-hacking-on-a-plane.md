---
title: "Hacking on a plane: Leaking data of millions and taking over any account"
layout: post
categories:
  - hacking
tags:
  - cybersecurity
  - hacking
---

![](https://i.imgur.com/6u4iy7e.png){: width="300" }
*Hacking on a plane, by Midjourney AI*

This is a short write-up about how I could have accessed the personal and financial information for tens of millions of users as well as take over anyone's account without user interaction. 

## Boredom leads to greatness

While on a 14-hour flight last week, after about 8 hours, I got tired of watching shows and reading books. I don't usually want to pay for WiFi, but I decided to check the price. If there is a flight to splurge on, it's a 14-hour one. 

When I pulled up my phone, I saw WiFi was provided by GoGo Inflight. I faintly recalled there being a bug bounty program on BugCrowd for them at some point. Before putting my credit card information and home address into an application, I often take a cursory glance at the security of the system. 

It allows you to register an account without putting in credit card data. So I created a test account, and browsed around to a couple pages before checking burp. The following request stood out to me due to the response containing all of my account information. Also, like any good bug hunter, the user_name field stood out as a potential IDOR.

```
GET /edge/apidecorator/v3/customer?data_types=PERSONAL,PMTINSTRUMENTS,GROUP_ATTRIBUTES
&requester=GOGO_INTERNET&tracking_id=uxdId-N510DN_A25AE4339A5309CCFA508534B9933
&user_name=testingz20221118213555&uxd_id=uxdId-_N510DN_A25AE4339A5309CCFA508534 HTTP/1.1
Host: gbp.inflightinternet.com
```

The thing about the username is that it's unguessable due to the timestamp. I decided to test it anyways by creating another account and using that username. I assumed that it wouldn't work or would restrict access. There's no way it would be that easy...

Tada! 🎉 It worked!

I still thought the impact was limited due to the `user_name` format, so I tried changing `user_name` to `email_address` since that was in the response... and it worked also. 

I tried `customer_id` since the IDs are integers. It would increase the impact from a targeted vulnerability (by email address) to disclosing all users by simply incrementing through all the IDs. That also worked!

## But wait, there's more!

I happened to check my personal email for an account. I assumed I had signed up for wifi with GoGo in the past before getting into security. Sure enough, I had an older account. And because I was already going to disclose a critical bug, I decided to check for another bug with that second account.

The password reset functionality used two requests. The first request was to 
`POST /edge/apidecorator/v2/customer/authenticate/` and validated the user's auth. After that, a PUT request to `/edge/apidecorator/v2/customer/` had this body:

```json
{
  "resetPassword": {
    "password": "password123!"
  },
  "user": "testingz20221118213555",
  "uxdId": "uxdId-GET /edge/apidecorator/v3/customer?data_types=PERSONAL,PMTINSTRUMENTS,GROUP_ATTRIBUTES&requester=GOGO_INTERNET&tracking_id=uxdId-N510DN_A25AE4339A5309CCFA508534B99332B0_1668735922_0avmL6L5q&user_name=testingz20221118213555&uxd_id=uxdId-_N510DN_A25AE4339A5309CCFA508534B99332B0_1668735922_0avmL6L5q HTTP/1.1_N510DN_A25AE4339A5309CCFA508534B99332B0_1668735922_0avmL6L5q"
}
```

I changed the `user` field to the username of my old account and was then able to login with the new password! Woah, it appeared to be a remote ATO without user interaction. 

I asked my friend Sam Curry if I could change his password as a test, just to be sure I wasn't making a silly mistake. Nearly all hackers have gotten confused thinking they had found an awesome bug only to realize they were actually only modifying their own account. Sure enough, it worked on his account as well!

## Impact

The impact of these two bugs was signifcant. It was access to first name, last name, address, and email of the user as well as last 4 digits, expiration date, billing name, and address of the credit cards. The customer IDs are in the tens of millions. Additionally, there was an account takeover vulnerability for all the accounts as well. 

Given PCI and GDPR compliance, these bugs in the hands of an attacker could have been disastrous. META was just fined €265 million for mass exposing the data of users. 

## Disclosure details

I looked around for a security contact at GoGo without much luck. Eventually I was pointed to the Airline ISAC. They were super helpful. Since I found the bugs while on a flight, they sent me a contact at that airline. Even though it was third-party, the airline worked with me to get it fixed. With their superb help, this was the timeline:

-  Monday (November 21st) the airline was made aware of the issue and immediately proceeded to escalate and contact the appropriate groups for validation and remediation.
-  Tuesday (November 22nd) the impacted third-party was formally debriefed, proceeded to confirm the validity of the findings, and began immediately working on a resolution.
-  Wednesday (November 23rd) the third-party stated their resolution has already been tested and deployed before noon Eastern.

I was flying back home that day and was able to validate the fix in the air, which was neat. Thanks for taking the time to read the post. I hope you enjoyed it. 

\- rez0


For more of my thoughts, bug bounty tips, and AI-generated hacker art, [follow me on twitter](https://twitter.com/rez0__). 

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://rez0.blog/hacking/2022/12/02/hacking-on-a-plane.html" />
<meta property="og:title" content="Hacking on a plane" />
<meta property="og:description" content="Leaking data of millions and taking over any account" />
<meta property="og:image" content="https://i.imgur.com/6u4iy7e.png" />
