---
title: "Operation Floodlight"
layout: post
categories:
  - hacking
tags:
  - hacking
  - cybersecurity
  - ai
---

![](/assets/images/operation_floodlight_banner_candidate_2_clean.jpg){: width="400" }
I have been thinking about the impact of AI system with strong cybersecurity capabilities. 

The United States has a lot of critical infrastructure that is obviously important: hospitals, water systems, power, transportation, telecom, financial services, food, dams, manufacturing, and all the other sectors [CISA lists](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).

A lot of that infrastructure has internet-facing software.

A lot of that software has bugs.

And a lot of those bugs are not in scope for any VDP or bug bounty programs.

That last part is the problem.

### Summary

[Miles Brundage wrote a proposal called Operation Patchlight](https://ifp.org/operation-patchlight/) about using advanced AI to help defenders find and fix vulnerabilities in open source code and critical infrastructure. Dane Sherrets at HackerOne recently told me about it.

I like it. I think it is targeting a real problem. But I think it should be more offensive in nature.

I would call it **Operation Floodlight**.

The US government should fund a national bug bounty grant program that pays researchers for verified vulnerabilities in US critical infrastructure, even when the affected asset is not already in scope for a normal bug bounty program.

Not every random bug. I mean real, reproducible vulnerabilities with real impact (Highs and Criticals only, for example).

Bugs like:
- Authentication bypass on a hospital device control system
- Access to all sensitive records in an emergency services portal
- Takeover of a critical vendor account used by local governments
- Remote code execution in exposed software used by water utilities
- Bugs that could disrupt critical operations if an attacker found them first

The simple version:

1. The government funds the program.
2. Trusted triagers validate the reports.
3. A protected disclosure process routes the bug to the owner.
4. The researcher gets paid.
5. The vulnerable organization gets help fixing it.

And all of this happens before opensource AI models have high quality vulnerability discovery capabilities.

I have written a lot about hackbots and AI-assisted vulnerability discovery. The cost of finding bugs is dropping. Eventually, things will be more secure, but a ton of critical infrastructure remains at risk. 

Either the United States gives good researchers a clean path to report serious findings, or more of those findings end up unreported, sold privately, used in an attack, or dumped publicly.

### Solution

Operation Floodlight would create a government-funded bounty layer for critical infrastructure bugs that are currently orphaned by the normal scope model.

It needs four parts.

### Pay hackers

Pay for verified impact, not for affiliation with an existing program.

If a vulnerability affects US critical infrastructure and meets the program's testing rules, the researcher should be eligible for a payout even if the affected organization never created a bug bounty program.

The reward should come from the grant pool, not from the hospital, water utility, county office, or small vendor that just got surprised with a security report.

### Protect good-faith research

The program would need clear safe harbor as many of the infrastructure owners are private companies. The researcher should be able to test and report without fear of legal action, as long as they follow the Government's program's rules.

This is the hard part, and it is probably the part lawyers will make less fun. 

The rules would probably have to be something like:

- No persistence
- No data exfiltration beyond the minimum evidence needed
- No destructive testing
- No social engineering
- No phishing
- No physical attacks
- No disruption of operational technology
- No testing that could affect patient care, public safety, power delivery, water treatment, transportation, or emergency response

If proving impact could cause harm, stop at the line and report the evidence.

### Route reports to the right owner

Disclosure is often harder than discovery. In this case, it's going to be MUCH harder. In fact, there should probably be bounties for finding the right owner of an asset.

Operation Floodlight should have a central intake, probably run through CISA or a CISA-backed partner. The intake team would:

- Validate that the issue is real
- Confirm the US critical infrastructure connection
- Identify the asset owner or vendor
- Coordinate disclosure
- Help the owner understand severity without panic
- Track remediation
- Pay the researcher after validation

This is basically a router for good-faith vulnerability reports.

The DoD already has useful precedent here. The [Defense Industrial Base Vulnerability Disclosure Program](https://www.dc3.mil/Missions/Vulnerability-Disclosure/DIB-Vulnerability-Disclosure-Program/) helps defense contractors receive and remediate vulnerability reports, and the program grew out of previous pilot work. That is not the exact same thing, but it proves the government can create a structured path between independent hackers and sensitive private-sector systems.

Floodlight would take that pattern and expand it to cover all critical infrastructure, not just defense contractors.

### Fund fixes, not just findings (optional)

One problem in all of this is that many legacy systems don't have great maintenance. Some critical infrastructure is running on old software, has weird vendors, or tiny teams, and getting it fixed will be a nightmare.

So Floodlight could include remediation grants.

Not giant blank checks, but enough of an incentive to get the right people to fix the problem. That could include:

- Emergency engineering support for severe bugs
- Vendor coordination help
- Short-term managed security support
- Funds to replace exposed legacy software
- Help writing disclosure-safe public updates when needed

This is where Operation Patchlight and Operation Floodlight fit together nicely.

Patchlight is more about giving defenders better tools and using AI to find and fix vulnerable code. Floodlight is about paying hackers to surface the bugs that otherwise sit in the dark.

Find the bugs. Fix the bugs.

### Implementation

Here is how I would structure it.

Pick a few sectors where the impact is obvious and the attack surface is messy: healthcare, water, emergency services, and maybe state or local government vendors that support those sectors.

Give the pilot a real budget. I do not care if the first version is $25 million, $100 million, or $500 million. The exact number is less important than the model.

Then set the payout bands high enough that quality hackers are willing to engage:

- High: $1,000 to $2,000
- Critical: $2,000 to $5,000

More would be better and yes, people will be upset no matter what. But I think an amount like this would make it feasible and still worth it for a researchers to find and report them.

The pilot should use professional triage. HackerOne, Bugcrowd, CISA's existing VDP infrastructure, DC3-style processes, trusted nonprofits, or some combination could all play a role. I am less attached to the way it's set up than the result. These organizations are already combating AI slop, so they should be equipped to handle the volume and quality of reports that will come in.

The program should also have a fast emergency lane. If a bug has obvious large scale public safety impact, route it fast, pay it fast, and get decision makers in the room fast to fix it. 

### The goal

The goal is simple:

Make it profitable and safe to report serious vulnerabilities in US critical infrastructure before attackers use them.

That is it.

\- Joseph

[Sign up for my email list](https://thacker.beehiiv.com/subscribe) to know when I post more content like this.
I also [post my thoughts on Twitter/X](https://x.com/rez0__).

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@rez0__" />
<meta name="twitter:creator" content="@rez0__" />
<meta property="og:url" content="https://josephthacker.com/hacking/2026/07/01/operation-floodlight.html" />
<meta property="og:title" content="Operation Floodlight" />
<meta property="og:description" content="A proposal for a government-funded bug bounty layer for serious vulnerabilities in US critical infrastructure." />
<meta property="og:image" content="https://josephthacker.com/assets/images/operation_floodlight_banner_candidate_2_clean.jpg" />
