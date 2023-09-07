---
layout: post
title: "Adventures in startups"
date: 2023-09-06
categories: startups work life lessons learned
---

As many of you readers my know, mostly are friends and family, I recently had spent the last 6 months working on a technology AI startup. Today I'm going to share with you the good, bad and ugly; then what I would do going forward.

Long story short, the company wanted me to put in significantly more effort then I could afford at no income. I was working 20 hours a week and my partners wanted me to scale that to 40 or more, as I was the "CTO" and this is "my company", I had to make sacrifices for it. Honestly, I hate the idea that I have to dedicate my entire life to pursue a startup, that if I don't I'm not good enough, qualified enough or passionate enough.

People like <a href="http://andyfrisella.com" target="_blank">Andy Frisella</a> work from 6 am to 11 pm every day, 7 days a week and preach that <a href="https://andyfrisella.com/blogs/andygram/quit-looking-for-balance-in-your-life" target="_blank">Balance doesn't exist</a>. Welp, it does and they're all wrong. Not everyone wants to be a billionaire working every second of every day to achieve the big industrialist dreams. I have no desire to be a tycoon, may a loon, but not a tycoon... I digres

# Lesson 1: Business partnerships are stupid and should be avoided

Yes, most business partnerships are stupid and should be avoided. I'll give you a great example from this startup, I had two major conflicts in the company. The first was the schedule, the second was my partners where making decisions that a CTO should be making not a COO or CEO. For example, making technical platform deicisions then telling engineers how to solve those problems and even what technology to use.

If you are the main technical resource building the platform, you should avoid taking on a business partner. My friend and boss, Patrick, put it this way. If you split a company with a non technical founder 50-50, you'll spend the first 3-9 months building the product. Then once the product is built, either your cofounder steps in, does their sales job. Or if they try to sell the product and are really terrible at it, you then go hire a sales person, now your co-founder benefits from you building the product, investing your capital to hire someone; they get the upside with no downside. You just wasted months of your time.

# Lesson 2: Don't make offers of employment until post funding or revenue

This was really stupid in hindsight. We offered to hire people at $30-50 an hour, all payable on an IOU. Welp, this isn't legal in any state. Employees cannot wave the right to be paid atleast minimum wage. Meaning you'll likely have to pay $15+ an hour to employees.

If you need help, offer equity. Never promise salaries, hourly pay or anything like that. It will cost you.

"But Adam, We're a C Corp!" -- It does not matter, in issues of payroll, I've had 3 attorneys tell me that payroll issues pierce the corporate veil. In the case of co founders, it means joint and several liability. Basically of John Doe, your partner can't pony up any money, you have to pony up all of it. Sucks to be you, right? You where the guy to build everything, they brought an intern to do who knows what, then they bail and leave you owing the intern, no sales and then fight you for equity/compensation whatever. To avoid, see my lesson 1.

# Lesson 3: Use an ORM

I did not use an ORM. I wrote all the SQL by hand, because I was a bad ass. I wrote joins, I wrote group bys, I let the DB do it's job. What happened? Diaster, updates didnt' work, keeping everything and everyone in sync sucked. Migrations exist for a reason. Data Models are great. ORMs allow you to more rapidly change the data model without having to re-write significant amounts of code. Stop being a know it all and use a ORM.

# Lesson 4: Hire an attorney to review everything

I did this after the fact and I learned that my founders agreement was garbage. I learned that most our filings and legal documents where full of holes and contradictions. Don't be cheap. Before you sign a thing, have someone with a law license that you pay money to review the document, better yet pay them to write the document.

# Lesson 5: Use cloud based tools

I let one of our partner's concerns about security & privacy for cloud based tools force us to run everything in a private cloud. Yes we used an AWS instance, but you had to use a VPN (wiregaurd) to login, and nothing hosted on a public service in a private account was allowed. Not only did we have more trouble managing our work load, we often had issues with SSH keys, email's getting marked as spam, connection issues with the VPN and much more. Self hosted Git, Redmine, Apache, MySQL, Email and more.

Use Trello, use Github or Bitbucket, use more then a cheap AWS instance, actually use RDS, CDK and other cloud resources. Not everyone will steal your IP.

# Lesson 6: Make your product easily affordable without approval

Yeah, enterprise customers exist, but ideally target a price in the $30-80 a month range Per XYZ. These types of purchases make it really easy for managers to swipe their company card without approval. Have multiple teirs but a basic product in this price range will pay the bills, validate your idea and give you time to grow.

# Lesson 7: Perfect is the enemy of done

I saw this in a friend, they spent 10 years building the perfect JS framework, then another 10 years perfecting it and released it to lackluster fare. They fought to make their product perfect and cover every single possible usecase. The trouble is, as you feature creep, you lose the ability to test if the market actually will pay for your product.

With my startup first it was an MVP, then it was a really complicated AI feature that had to be perfect (Still in progress), then refinements to our core product, then a bunch of other new features before we could really approach investors or customers. We had a kick ass demo and a really nice product, but no sales, no investment. Just slick stuff.

Fail early, fail often. Test your ideas, just like <a href="https://theleanstartup.com" target="_blank">The Lean Startup</a>.

# Lesson 8: If it's not core to your product, pay for it

A great example of something we did well is we used <a href="https://www.propelauth.com" target="_blank">Propel Auth</a> to manage our login pages, our login process, 2 factor auth and all the user setup and multi tenant. There are a lot of places in our application that were not the core part of the business, where we should have just subscribed to the free / cheap plan, built the MVP of that feature and tested it to see if the solution was the right type of solution.

# Lesson 9: Relax

Someone has the same idea as you. They will solve it in a similar way, they will raise money, they will get customers, they will likely be successful but so can you. If the idea is sound, the model is solid and the execution is good, you can and will find customers, investors and partners. If there's no competition in the market, either you've found an island where there is gold to be found, are brand new to the market (AI or Crypto for example) or have not looked hard enough. Competitors exist. That's a good thing. Someone will hate your solution and they will love your competitor. Someone will hate your competitor and love you. Deal with it.

Time to market is important but if your success depends on getting the application done yesterday, investment done last week and customers a month ago, did you really have a reasonable shot at success? I doubt the cards are that stacked against you. It's ok to take some time, not to much (see lesson 7). Relax it's a marathon not a sprint.

# Lesson 10: You will be dead in 100 years

<a href="http://www.adambourg.com/interesting/not-mine/2023/08/28/we-will-all-be-dead-soon.html" target="_blank">You will be dead in 100 years, what does the work you do today matter in the long run? </a>
