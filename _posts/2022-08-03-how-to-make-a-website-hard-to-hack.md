---
title: "how to make a website hard to hack"
layout: post
categories:
  - hacking
  - cybersecurity
tags:
  - hacking
  - cybersecurity
---

![](https://i.imgur.com/qOdpjdg.png){: width="300" }

I have hacked on thousands of websites and learned a bit about what makes a hacker's job more difficult. Simple design decisions can be a security multiplier as well as cut down on the quantity and complexity of security checks. What follows is a list of design decisions that add significant security impact. 

## me-based authorization

This is what I call it when an API is deciding what data to return based on the auth mechanism for that user (cookies or authorization headers generally), rather than a parameter or path. This increases security significantly because it cuts down on the IDOR protection that is required. 

**Indication this is implemented:** API endpoints are generic like `/api/v1/me` or `/api/v1/account` and only return your data. The alternative would be a path such as `/api/v1/account/1337` or `/api/v1/account?id=1337`. This can still be secure, of course. But any hacker will tell you that it's less likely to be so.

**Note**: There may be a term for this design principle. If so, please let me know on [twitter](https://twitter.com/rez0__). 

## simple rbac

The most difficult-to-hack websites are those with simple permission schemes. A good example would be a site that has only users and admins. Or an application with admins and read-only accounts. 

Role-based access control significantly increases complexity. Complexity increases the chance of vulnerabilities. If you add a new role, you now have to validate (and continually test) every single piece of functionality that the new role should and should not be able to perform. This is further complicated if you have granular permissions or the ability to grant cross-tenant access.

**Indication this is implemented:** Self-evident in the permission scheme.

## org-based data segregation

Cross-org (or cross-tenant) data access is often the most impactful vulnerability during an assessment. The fall out of an employee at a company escalating to admin is often not as high as a user being able to access or modify the data for all organizations. 

Whether or not the data segregation is separate hardware or just separate indices in a flat database doesn't matter too much. Can the application _ever_ access data cross-org? A useful thought exercise might be to ask yourself or the developers: How hard would it be to modify the code such that one org _could_ access data from another org?

**Indication this is implemented:** It's often hard to tell. One way I've observed this to be evident is when there's a request such as `/api/v1/org/52452345/details` and changing the org ID results in a 404 rather than a 403 or 401. 

<img alt="hacker" src="https://i.imgur.com/aI0guMM.png" width="250px" style="display: block; margin-right: auto; margin-left: auto;"/>

## single sign-on everywhere

Not being able to even _access_ any website for a company makes it extremely difficult, if not impossible, to hack. If I'm testing a company without credentials and all their sites simply redirect to single sign-on, there's not a lot to test. It severely limits the options available to the hacker, which is great for security.

**Indication this is implemented:** When browsing to all the different domains a company owns, you get redirected to an SSO page such as Okta. 

## site-wide CSRF tokens

This one is a bit more implementation-based rather than a design decision, but it's worth including due to the number of times I've seen it implemented in a non-systemic way. For example, when a company only implements CSRF protection on sensitive sites or sensitive API endpoints, there are often gaps. Or if there aren't gaps now, future features will end up lacking CSRF protection. By properly implementing it site-wide as a policy, CSRF as a bug class can be removed as a possibility.

**Indication this is implemented:** When browsing a variety of pages on multiple domains and API hosts, every request has a CSRF token as a header. 

## thanks

I appreciate your time. To keep up with new posts, you can add this site to feedly or just [follow me on twitter!](https://twitter.com/rez0__) 


\- rez0

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://rez0.blog/hacking/2022/08/03/how-to-make-your-website-hard-to-hack.html" />
<meta property="og:title" content="how to make a website hard to hack" />
<meta property="og:description" content="how to make a website hard to hack" />
<meta property="og:image" content="https://rez0.blog/assets/images/bubble.png" />
