# Postmortem: The Great Website Outage


![TEXT ATL](Debaclehttps://sf16-va.tiktokcdn.com/obj/eden-va2/nb-shivsn-ryhs/ljhwZthlaukjlkulzlp/lark-topics/project-management-methodologies-for-functional-teams/enterprise-modeling-for-design-and-user-experience-teams.webp)


# Issue Summary:

Duration: From 10:00 AM to 11:30 AM on May 10, 2024 (UTC), our website took an unplanned siesta.

Impact: Picture this: our primary e-commerce website decided to play hide-and-seek with our users. Roughly 80% of them were left scratching their heads, staring at loading screens or cute little error messages
.
Root Cause: Turns out, our trusty load balancer got a little too enthusiastic and started sending traffic on a wild goose chase, forgetting to share the load properly.

# Timeline:

10:00 AM (UTC): Cue the dramatic music! Our monitoring system went berserk, screaming about unusual latency and error rates on the website.
10:05 AM: Engineers stumbled out of their morning coffee haze and noticed the website gasping for air under a sudden flood of traffic.
10:15 AM: Initial investigation pointed fingers at the usual suspects: web servers and databases. Were they misbehaving? We needed to find out!
10:30 AM: Suspicions turned toward a DDoS attack as traffic surged like a horde of hungry zombies. Quick, raise the network security drawbridge!
10:45 AM: The cavalry, a.k.a. The network infrastructure team arrived as we zeroed in on the load balancer as the potential culprit.
11:00 AM: After digging through load balancer logs, we caught it red-handed, misrouting traffic like a GPS with a sense of humour.
11:30 AM: Victory! We wrestled the load balancer into submission, reconfiguring it to play fair and evenly distribute traffic among our servers.

# Root Cause and Resolution:

Root Cause: Our trusty load balancer got a little too excited and decided to play favourites, sending some servers on a vacation while overloading others.

Resolution: With a firm hand and a gentle touch, we corrected the load balancer's mischievous ways, ensuring it properly shared the traffic love among all our servers.

# Corrective and Preventative Measures:

# Improvements/Fixes:
Schedule regular load balancer configuration check-ups to catch any potential misconfigurations before they cause chaos.

Spice up our monitoring systems to keep an eagle eye on traffic patterns and load balancer behaviour.

# Tasks to Address the Issue:
Conduct a load balancer configuration deep-dive to sniff out any other potential troublemakers lurking in the shadows.

Cook up some automated scripts to babysit our load balancer and prevent future misconfigurations from crashing the party.


This postmortem isn't your average tech document.ama, suspense, and a pinch of humour, we've brought our website outage saga to life. So next time you're debugging a digital disaster, remember: a little laughter goes a long way!

