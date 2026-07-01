---
title: "Operation Floodlight"
layout: post
published: false
categories:
  - hacking
tags:
  - hacking
  - cybersecurity
  - ai
---

![](/assets/images/operation_floodlight_banner_candidate_2_clean.jpg){: width="400" }

I have been thinking about a weird gap in bug bounty for a while.

The United States has a lot of critical infrastructure that is obviously important: hospitals, water systems, power, transportation, telecom, financial services, food, dams, manufacturing, and all the other sectors [CISA lists](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors).

A lot of that infrastructure has internet-facing software.

A lot of that software has bugs.

And a lot of those bugs are not in scope for anything.

That last part is the problem.

If a hacker finds a serious vulnerability in a random US hospital vendor, municipal water utility, regional power provider, emergency services portal, or logistics company, there is often no good path. Maybe there is a security.txt. Maybe there is a contact form. Maybe there is a lawyer-shaped brick wall with a "do not test us" sign on it.

So the incentive is backwards. We want good hackers to find and report the bugs that matter most, but the current system often says:

"Please only help if the organization already had the budget, knowledge, and legal comfort to invite you."

That is not how national defense should work.

### Summary

[Miles Brundage wrote a proposal called Operation Patchlight](https://ifp.org/operation-patchlight/) about using advanced AI to help defenders find and fix vulnerabilities in open source code and critical infrastructure. Dane Sherrets at HackerOne recently pointed me to it.

I like it. I think it is pointed at a real problem.

But there is another version of this idea that is more native to the hacker economy.

I would call it **Operation Floodlight**.

The US government should fund a national bug bounty grant program that pays researchers for verified vulnerabilities in US critical infrastructure, even when the affected asset is not already in scope for a normal bug bounty program.

Not every random bug. Not "I ran nuclei and found a missing header." Not "I saw a 403 on /admin." Please spare all of us.

I mean real, reproducible vulnerabilities with real impact:

- Authentication bypass on a hospital scheduling system
- Access to sensitive records in an emergency services portal
- Takeover of a critical vendor account used by local governments
- Remote code execution in exposed software used by water utilities
- Bugs that could disrupt critical operations if an attacker found them first

The simple version:

1. The government funds the bounties.
2. Trusted triagers validate the reports.
3. A protected disclosure process routes the bug to the owner.
4. The researcher gets paid.
5. The vulnerable organization gets help fixing it.

The point is not to replace existing bug bounty programs.

The point is to catch the important bugs that fall between them.

### Motivation

Bug bounty scope is not the same thing as risk.

Scope is a contract boundary. Risk is reality.

Those two overlap sometimes. They do not overlap enough.

Every experienced bug hunter knows this. You find an asset. You trace ownership. You realize it belongs to something sensitive. Then you check the program page and it says the asset is out of scope, or the company has no program, or the only visible policy says they might sue you for looking too closely.

So you stop.

That is legally rational. It is also kind of insane.

Attackers do not stop because the asset is out of scope. Ransomware crews do not check the policy page. Foreign adversaries do not care whether a hospital vendor joined a VDP. If the bug exists, they can use it.

Meanwhile, the people most likely to find these issues before the bad guys are trained to walk away.

This gets worse with AI.

I have written a lot about hackbots and AI-assisted vulnerability discovery. The cost of searching for bugs is dropping. Coverage is going up. More weird attack surface will be mapped. More one-off vendor systems will be poked by humans, agents, and human-agent hybrids.

That can go two ways.

Either the United States gives good researchers a clean path to report serious findings, or more of those findings end up unreported, sold privately, burned in crime, or dumped publicly after someone gets frustrated.

I know that sounds dramatic, but I do not think it is. It is just incentives.

### Solution

Operation Floodlight would create a government-funded bounty layer for critical infrastructure bugs that are currently orphaned by the normal scope model.

It needs four parts.

### Pay hackers

Pay for verified impact, not for affiliation with an existing program.

If a vulnerability affects US critical infrastructure and meets the program's testing rules, the researcher should be eligible for a payout even if the affected organization never created a bug bounty program.

The reward should come from the grant pool, not from the hospital, water utility, county office, or small vendor that just got surprised with a security report.

That matters.

If the asset owner has to pay the bounty, they may fight the report. If the government pays, the owner can focus on fixing the bug. The researcher can focus on quality. The triager can focus on truth.

This also avoids turning every report into an awkward shakedown-flavored conversation with an organization that never opted into bug bounty.

Nobody wants that. Or at least nobody normal wants that.

### Protect good-faith research

The program would need clear safe harbor.

This is the hard part, and it is probably the part lawyers will make less fun. Still, it is required.

The rules should be strict:

- No persistence
- No data exfiltration beyond the minimum evidence needed
- No destructive testing
- No social engineering
- No phishing
- No physical attacks
- No disruption of operational technology
- No testing that could affect patient care, public safety, power delivery, water treatment, transportation, or emergency response

If proving impact could cause harm, stop at the line and report the evidence.

For example, if you find an unauthenticated endpoint that appears to control something in an industrial system, you do not press the big red button because you are "validating impact." You document the exposure, show the access boundary failure, and let the triage team coordinate with the owner.

Good hackers already understand this.

The point of safe harbor is not to legalize reckless testing. It is to protect careful reporting when a real issue crosses the researcher's path.

### Route reports to the right owner

Disclosure is often harder than discovery.

I have found plenty of bugs where the technical part was easier than figuring out who owned the thing and who would actually read the email.

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

Floodlight would take that pattern and aim it wider.

### Fund fixes, not just findings

Paying for bugs is not enough.

Some critical infrastructure organizations can fix a report quickly. Others are running old software, weird vendors, tiny teams, and procurement processes that feel like they were designed by someone who hates calendars.

So Floodlight should include remediation grants.

Not giant blank checks. Practical help.

- Emergency engineering support for severe bugs
- Vendor coordination help
- Short-term managed security support
- Funds to replace exposed legacy software
- Help writing disclosure-safe public updates when needed

This is where Operation Patchlight and Operation Floodlight fit together nicely.

Patchlight is more about giving defenders better tools and using AI to find and fix vulnerable code. Floodlight is about paying hackers to surface the bugs that otherwise sit in the dark.

Those are complementary.

Find the bugs. Fix the bugs.

Very complicated, apparently.

### Implementation

Here is how I would build it.

Start with a pilot.

Pick a few sectors where the impact is obvious and the attack surface is messy: healthcare, water, emergency services, and maybe state or local government vendors that support those sectors.

Give the pilot a real budget. I do not care if the first version is $25 million, $100 million, or $500 million. The exact number is less important than the model.

Then set the payout bands high enough that serious hackers pay attention:

- Low: usually no payout, unless there is a clear critical infrastructure angle
- Medium: $1,000 to $5,000
- High: $5,000 to $50,000
- Critical: $50,000 to $250,000+

And yes, I know people will argue about those numbers.

Good.

The point is to make the market care. A critical bug in critical infrastructure should not pay less than a coupon leak on a shoe website.

The pilot should use professional triage. HackerOne, Bugcrowd, CISA's existing VDP infrastructure, DC3-style processes, trusted nonprofits, or some combination could all play a role. I am less attached to the org chart than the result.

Reports should be judged by impact:

- Can an attacker access sensitive data?
- Can an attacker modify critical data?
- Can an attacker disrupt operations?
- Can an attacker move from a vendor into a critical infrastructure owner?
- Can the bug scale across many organizations?
- Is the affected system exposed to the internet?
- Is there evidence that similar bugs are being exploited in the wild?

The program should also have a fast emergency lane. If a bug has obvious public safety impact, route it fast, pay it fast, and get adults in the room fast.

That part matters. Nothing kills researcher trust like sending a serious report into a queue and hearing nothing for six weeks.

### What about consent?

This is the obvious objection.

Companies did not opt in. So why should researchers be allowed to test them?

My answer is: they should not be allowed to "test them" in the broad bug bounty sense.

Floodlight should not authorize open season on every hospital, water plant, power provider, or vendor in America. That would be stupid, chaotic, and probably a great way to make everyone hate hackers more.

The program should protect good-faith, limited, non-destructive research when the researcher encounters a real issue and reports it through the right path.

That is a narrower thing.

Think of it less like "the government created a bounty on your company" and more like "the government created a safe reporting and payment path for serious vulnerabilities affecting national infrastructure."

Asset owners should also be able to onboard after a report. First report comes through Floodlight. Then the organization gets offered a managed disclosure process, remediation help, and maybe a path into a normal VDP.

The goal is not to surprise people forever.

The goal is to make the first contact less awful.

### What about noise?

This is the second obvious objection.

If you pay for out-of-scope bugs, people will submit junk.

Correct. They will.

Bug bounty already has this problem. Every public program gets junk. The answer is not to avoid the model entirely. The answer is strict triage, clear standards, researcher reputation, rate limits, duplicate handling, and ruthless rejection of low-signal reports.

Floodlight should not pay for:

- Missing SPF
- Clickjacking on a static page
- Public version banners
- "Sensitive file found" when the response is a generic 403
- Scanner output with no proof
- Self-XSS with no path to impact
- Theoretical supply-chain essays with no exploit

POC or GTFO, basically.

National security edition.

### The goal

The goal is simple:

Make it profitable and safe to report serious vulnerabilities in US critical infrastructure before attackers use them.

That is it.

We do not need to pretend this solves all cybersecurity. It will not.

Some organizations still need better asset inventory. Some need MFA. Some need patching. Some need vendors who answer email. Some need to replace software that should have been retired when Lost was still on TV.

But Floodlight would fix one very specific broken incentive:

Right now, many of the best hackers in the world are financially rewarded for finding bugs in companies that already know how to buy bug bounty, while some of the most important systems in the country sit outside the reward structure.

That is backwards.

Point the money at the risk.

Point the hackers at the risk.

Point the light at the risk.

Floodlight.

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
