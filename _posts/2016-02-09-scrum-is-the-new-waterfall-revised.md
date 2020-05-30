---
title: Scrum is the new waterfall (REVISED)
date: 2016-02-09T07:00:06+00:00
author: adam.bourg@gmail.com
layout: post
permalink: /2016/02/09/scrum-is-the-new-waterfall-revised/
categories:
  - Uncategorized
---
Over the last few months, I&#8217;ve gotten a <a href="https://news.ycombinator.com/item?id=10543180" target="_blank">TON</a> of <a href="https://www.reddit.com/r/programming/comments/3sc21s/scrum_is_the_new_waterfall/" target="_blank">feedback</a> from my post in November, &#8220;Scrum is the new waterfall&#8221;. Some of the feedback was good and others really thought my perspective is extremely negative.

After reading all the feedback and considering it, my arguments were not concrete enough to make a strong case for my strong opinion. One of the things I learned is that scrum is done very differently across different companies.

Lets revise my post.

**What are the main problems with adopting any new processes? **

  1. No buy in from leadership. I&#8217;ve worked on several projects in the last 2 years at my company now where the &#8220;business&#8221; or leadership team don&#8217;t buy into the belief that doing things iterative in an organized fashion will produce better software. Buy in & support from whoever is paying you is the first key to being successful in implementing whatever new process you&#8217;re adopting.
  2. There is no buy in from the team. Recently I worked with a team that didn&#8217;t want to change. They were used to the crazy and old way, the mid night deploys and code constantly breaking. Without team member and leader buy in, there will be no progress in making forward change.
  3. The perceived need isn&#8217;t there. Things work well, we ship code and make money, why are people complaining? Sure it might not be ideal, but hey, nothing is ever ideal.

**What is scrum? **

Scrum is a process. It&#8217;s a way to get work done. There are iterations to deliver software to the customer very quickly. From my perspective the value of scrum to the business and leadership is predictability. Within a reasonable perspective, we can estimate that we can deliver x software in y amount of time. While that sounds great and reasonable, often that is not the case.

**What is the motivation of scrum?**

From the <a href="https://www.scrumalliance.org/" target="_blank">Scrum Alliance</a> we get the following definition of scrum:

> Scrum is a simple yet incredibly powerful set of principles and practices that help teams deliver products in short cycles, enabling fast feedback, continual improvement, and rapid adaptation to change.

**How can scrum become waterfall? **

Scrum can become watefall-y in certain situations. Such as:

  1. The ceremonies are more important then the work getting done. This is especially important when Standup serves as a status meeting to notify and justify management that the developer team is getting work done. Standups aren&#8217;t for management to get a status update, thats what the Kanban is for, the standup is to help move the team along.
      1. Other ceremonies such as planning and grooming, while important, if it drags to many engineers away it can make the process burdensome.
      2. There should be a natural balance between how many meetings and the effectiveness of those meetings and the ability to move the team forward.
  2. &#8220;It&#8217;s just a small change&#8221;. This is really important, Scrum is about delivering working software on a schedule. When someone comes to you asking you to deliver work outside of the scope of the sprint, you need to push back to your scrum master and team. Small changes can quickly become big headaches for teams.

The core problem I have with Scrum is it feels &#8220;Anti Agile&#8221; but in the cloak and dagger of actually being Agile. The key parts of this argument come from the Agile <a href="http://www.agilemanifesto.org/" target="_blank">manifesto</a> itself:

> <span style="font-size: medium;">Individuals and interactions </span><span style="font-size: small;">over processes and tools<br /> </span><span style="font-size: medium;">Working software </span><span style="font-size: small;">over comprehensive documentation<br /> </span><span style="font-size: medium;">Customer collaboration </span><span style="font-size: small;">over contract negotiation<br /> </span><span style="font-size: medium;">Responding to change </span><span style="font-size: small;">over following a plan</span>

The key points are, can you prioritize people and the interactions instead of the processes? Can you respond to change really fast? Can you deliver real working software?

**How do I actually be Agile?**

It&#8217;s my belief that there are several components both technical and philosophical to actually being Agile.

  1. Philosophical:
      1. Ensure that the leadership and team have by into delivering software that&#8217;s high quality really fast. It&#8217;s better to keep delivering software small chunks at time so that you can quickly get feedback.
      2. Focus on communicating the needs that are changing and prioritize the team to work smart and solve the most important &#8220;Minimum Viable Produce&#8221; path first, then iterate on the second things that need to change.
      3. Get the client onboard, get them to be apart of the feedback cycle, and deliver real software on a continual basis.
  2. Technical:
      1. Write <a href="http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882" target="_blank">clean</a>, <a href="http://misko.hevery.com/code-reviewers-guide/" target="_blank">testable</a> code.
      2. Configure your build process to catch bugs by running tests, automate deployments to QA / STAGE and create an approval process that automates the deployment to production.
      3. Create automated &#8220;Black Box&#8221; style tests that utilize the behavior of the code you&#8217;re testing. Think about the public contracts it must enforce, test strictly those. Unit tests are worthless, test the contracts.
