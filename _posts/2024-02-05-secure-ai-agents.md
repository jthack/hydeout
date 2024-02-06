---
title: "From Concept to Capability: Required Security Changes for Secure AI Agents"
layout: post
categories:
  - ai
tags:
  - cybersecurity
  - ai
---

![](https://i.imgur.com/dXiJCDT.jpeg){: width="400" }
Capable AI agents will require new infrastructure. In order to expedite the utility of digital assistants by granting human-like access to them, we need founders devoted to solving API-ification of legacy systems, hardened sandboxes for AI agents, and agent authentication.

The libraries and frameworks for AI systems are pretty immature right now. Most applications are simple chatbots or forms of retrieval. But as we increase the complexity of the use-cases, the current architecture won't be sufficent. Anyone who has spent a few minutes thinking about AI has considered how useful it would be to have a cheap personal assistant that could tackle complex tasks or how much money it would save businesses if they were able to replace significant headcount with AI agents.

## Example Tasks
For a pesonal use case, we can imagine the task of ordering some food for pickup from a restaurant. A workplace example might be: Go into the AWS console, spin up a virtual machine, and install a specific opensource project in it. These are real tasks that someone would want to give to a real assistant.  

For nearly every system that an agent would need to interact with to accomplish a task, there has to be an API or credentialed UI access (the capability to browse to the application with those credentials similar to how a human would). The infrastructure to do most of that doesn't exist right now. Let's showcase that through the examples above. 

For the **food example**, the AI needs:
- The interests of the user. This can be solved with current memory systems, the prompt itself, or personal API.
- A way to list the restaurants. I'm not sure if Google has an API for this. They probably do. 
- A way to list the menu items. There's no API right now, but I think this would be a fantastic start-up idea. Scrape all restaurants websites for menus and build an always updating third-party menu API that agents can hit when trying to order food or answer users' queries about menus. 
- A way to hire someone to pick up and drop off the food. I doubt this exists currently, but DoorDash and UberEats should add it. The agent would need credentials.

For the **AWS example**, the AI needs:
- Credentials to access AWS, either an API token or login creds.
- A way to navigate through the console if APIs don't exist for desired functionality. 
- A way to look up the open-source project and install it on the virtual machine.

I think the most secure, efficicent, and accurate infrastructure would be entirely API-based, but I don't see us getting there soon. And AI agents are too valuable for us to "just wait" for the API-ification to be better. So what do we do? We build both. 

The most popular "AI Device" stand-alone device was recently launched. It's called the Rabbit R1. [In the Rabbit R1 keynote](https://www.rabbit.tech/keynote), they reveal that they have made a credentialed sandbox virtual machine for the AI to use to accomplish tasks. In the keynote, he says you'll just sign in to your personal accounts during an onboarding flow, and it'll be stored securely, etc. Personally I find it quite unsafe to grant an AI agent access to my services. Prompt injection in that setup would grant an attacker full control of all the credentialed applications.

![](https://i.imgur.com/6nPI4eB.png){: width="400" }
## Solutions
Here's how I think we could solve each of the limiting factors for good and secure AI agents.

### Credentialed UI Access
So let's assume the agent needs access to a service without a functional API. To securely give the agent credentialed access, it requires a few things:
- A Hardened Sandbox: No one wants an attacker to get access to a VM which is logged into every service.
- Delegated Accounts: A way to give agents their own accounts for services. This will often require the next bullet.
- AI-Specific Phone Numbers and Emails: In order for agents to be able to verify MFA and access confirmation emails, they'll need their own number and email. This doubles as a safety barrier since granting an agent access to one's personal email is unwise.
- Step-up Approval Features: Critical actions where the agent is spending money or changing settings should initially require user approval until extremely high accuracy is achieved.

### Authentication for Agents
We need to find a way to grant an AI agent authorized access to various services. Traditional authentication methods are not well-suited for agents as it would require using your own personal information for the agent's account on the service if you decided it was unsafe to use your own. At that point, you're creating two accounts on every service with your own data or fake data, which will often break the terms of service. Even if it doesn't, you're managing multiple email addresses or
something else weird.

To address this issue, I think a new authentication framework is needed (or something built on top of OAuth, etc). The framework could include some or all of the following components:

1. Agent Identity Verification: Each AI agent should have a unique identifier that can be verified by the services it interacts with. This identifier could be a digital certificate or a token issued by a trusted authority.
2. Delegated Authorization: Users should be able to grant specific permissions to AI agents, allowing them to perform certain actions on their behalf. This can be achieved through a mechanism similar to OAuth (or just OAuth), where users authorize agents to access specific resources or perform specific tasks without sharing their credentials through the use of scopes.
3. Audit Logging: All actions performed by AI agents should be logged for user review at any time. This will help to debug and ensure quality, allowing users to review and change permissions if necessary.

### API-ification
One of my favorite ideas for enabling AI agents to perform more complex tasks is through automated API-ification of services that currently lack one. A good example of this is the restaurant industry, where menus and prices change, and every restaurant isn't going to develop and maintain their own API. However, there is an opportunity for a third-party to come in and do it.

A company could use an LLM with vision capabilities to parse restaurant menus from various sources, such as websites, social media, or even photos of physical menus in reviews. By using vision models, the company could extract relevant information from the menus and present it in a standardized API format. This API would then be accessible to AI agents, allowing them to query the latest menu items, prices, and specials from any restaurant.

This is just one example. There are other industries where similar API-ification would unlock new AI agent functionality.

## Conclusion
So yeah, getting human-like capabilities in our AI agents securely will require new infrastructure. We need to create hardened sandboxes for secure UI access, potentially build authentication protocols made specifically for AI agents, and start chipping away at the API problem. 

Which part will you build?

Thanks,   
\- Joseph

To know when I drop a new post, [join my email list](https://thacker.beehiiv.com/subscribe). 

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/ai/2024/02/06/secure-ai-agents.html" />
<meta property="og:title" content="From Concept to Capability: Required Security Changes for Secure AI Agents" />
<meta property="og:description" content="Why we need secure sandboxes, agent-based authentication, and more APIs." />
<meta property="og:image" content="https://i.imgur.com/dXiJCDT.jpeg" />

