---
layout: post
title: "A programmers approach to building a sprinkler system"
date: 2023-08-23
categories: gardens hobbies water
---

Back in April of 2022 we moved into a new house, giant house, mcmansion really (3400 sq ft across 2 levels). The lot is really massive, probably atleast 10-15,000 sq ft. Both the front and backyards lacked an automatic irrigation system not to mention the landscaping consisted of mostly weeds. Being cheap and very lazy, I set out to do my best to automate systems to care for my massive yard without the hassle of hiring a contractor and having them build a crappy system.

In recent years, I've found I generally hate residential contractors. If you have any major work done, expect to supervise them the way you'd supervise a 3 year old child. Bid after lame bid, I kept getting price tags of between $10,000 and $15,000 to do some simple things to my yard. Put in some mulch, plant some bushes and run some poly tubing. The margins are great for these builders. I being of the mind that almost anyone can figure it out so why shouldn't I be able to do it, have grown in my abilities in tackling projects of various sizes.

Last summer was a successful experiment, could I keep my lawn green and thriving with a hose and a few simple timers? Yes I could. The front was ONLY 20' by 50', a whopping 1000 square feet, so it was hardly a challenge. My backyard is massive, atleast 100' feet by 70' feet in many places. The grass covers a minimum of 2500 square feet. Why am I putting water on it while I live in Colorado like a silly American? Because I'm an American, and I want the yard to be pretty.

I didn't want to bury or run tubing, for a variety reasons not including having to call 811, it's a lot of work among many other reasons. The biggest of which in my old house, inspite of yearly blow outs my automatic system ALWAYS had a major malfuction typically running $500 to $1000 to bring the system online, then a few hundred a month to figure out if I was watering enough or not.

# The system

![The facet](/assets/img/2023-08-23-facet-by.jpg)

To prevent pouring $1000 a year on startup costs, I built my own system using hoses and timers. The way it works is like this:

1. My facet on the west side of the house has a timer with 2 zones. Zone 1 runs sprinklers 1 and 2, approx 10' and 20' feet away. These run daily at 7:30 am for 15 minutes. This zone covers about 50% of my grass.
2. Zone 2 runs in a 100' foot hose to the east side of my yard, it feeds into a 4 port timer that feeds into 4 seperate sub systems.

## The east side system

![the east system](/assets/img/2023-08-23-sub-system.jpg)

The east side system has 4 major zones:

1. Garden beds using 1/4 inch soaker tubing for growing flowers, veggies and other things.
2. The hanging baskets off of our pergola.
3. The remaining 50% yard sprinkler.
4. The newly mulched yard with our perennial flower garden plant on drip lines.

# How do I get timing right with a zone inside another zone using 2 timers?

Here's the timing table for the main timer from the facet:
| Zone | Duration | Scheduled Time | Role Description | Frequency |
| ---- | ---------- | -------------- | -------------- | --------- |
| 1 | 30 minutes | 7:30 am | The west side of the yard's 2 sprinklers for the watering of the grass | MWFS |
| 2 | 90 minutes | 5:15 am | The primary timer zone for the east zone, so we can water the other sub zones | Daily |
| 2 | 30 minutes | 8:30 pm | The east side has a drip timer for just the raised garden beds to ensure enough water | Daily |

Here's the timing table for the east side:

| Zone | Duration   | Scheduled Time | Role Description | Frequency       |
| ---- | ---------- | -------------- | ---------------- | --------------- |
| 1    | 15 minutes | 5:15 am        | Raised beds      | Daily           |
| 1    | 30 minutes | 8:30 pm        | Raised beds      | Daily           |
| 2    | 15 minutes | 5:30 am        | Hanging baskets  | Every other day |
| 3    | 40 minutes | 6:00 am        | Grass            | MWFS            |
| 4    | 15 minutes | 6:30 am        | Perennial garden | Daily           |

The nice thing about this system is that if I need to skip days, all I need to do is set the main Zone 1 to water on a different schedule and it will affect everything downstream. Also if I wanted to add a general purpose fertlizer I could at the base of the system.

# Parts List

The system is pretty straight forward, but below is a break down of the parts you would need to build something similar.

| Qty | Price | Item                                                                                                                                                                                                                                                                                        | Reason                                                                                                                                                                                                   |
| --- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | $34   | 2 Zone Timer                                                                                                                                                                                                                                                                                | [This is for the main facet](https://www.amazon.com/Sprinkler-Programmable-Watering-Irrigation-Automatic/dp/B0C1GJ3BHK/ref=sxin_16_pa_sp_search_thematic_sspa)                                           |
| 1   | $64   | 4 zone timer                                                                                                                                                                                                                                                                                | I would buy [two](https://www.amazon.com/Melnor-65140AMZ-Digital-Timer-Yellow/dp/B09YZ2782J) of these instead of the 2 zone and the 4 zone, that way you have more flexibility on both sides of the yard |
| 1   | $40   | 100' hose                                                                                                                                                                                                                                                                                   | I would buy one of these at a local store, very expensive online                                                                                                                                         |
| 3   | $20   | 25' hose                                                                                                                                                                                                                                                                                    | I would buy a few of these and some male/female connectors so you can size them to your yard                                                                                                             |
| 1   | $5    | Hose y splitter                                                                                                                                                                                                                                                                             | For allowing you to bypass for regular hose usage                                                                                                                                                        |
| 1   | $8    | Backflow preventer                                                                                                                                                                                                                                                                          | To prevent back up from the system to flow into your main water line                                                                                                                                     |
| 1   | $15   | 100' 1/4 Poly Tubing                                                                                                                                                                                                                                                                        | For drip lines at the plant level                                                                                                                                                                        |
| 1   | $30   | 100' 1/2 poly tubing                                                                                                                                                                                                                                                                        | For bringing water to an area for using with a drip line                                                                                                                                                 |
| 1   | $10   | [100 count drip sprayer](https://www.amazon.com/Irrigation-Dripper-Sprinklers-Adjustable-Watering/dp/B07QNWXPJ8/ref=sr_1_8?keywords=drip+sprayer&qid=1692824290&sr=8-8)                                                                                                                     | Great for hanging pots, and general use in watering the plants, not for lawns                                                                                                                            |
| 1   | $12   | [Drip 1/4 soaker hose](https://www.amazon.com/Raindrip-015005T-4-Inch-50-Feet-Porous/dp/B000LNSX82/ref=sr_1_5?crid=IMX5788F94FZ&keywords=drip+soaker+line&qid=1692824365&sprefix=drip+soaker+line%2Caps%2C157&sr=8-5)                                                                       | Really helpful for garden beds                                                                                                                                                                           |
| 3   | $16   | [Large Sprinkler spinning](https://www.amazon.com/Sprinkler-Adjustable-Irrigation-Oscillating-Connection/dp/B07D2ZY411/ref=sr_1_13_sspa?crid=3REAZ3LNPW0AL&keywords=2%2Bzone%2Btimer&qid=1692823833&sprefix=2%2Bzone%2Btimer%2Caps%2C253&sr=8-13-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&th=1) | This thing is great, I have a hodge podge of sprinklers and I would standardize on 3 of these                                                                                                            |

All in probably close to $350 worth of parts and moving pieces. It's a bit complicated to get setup, but look at these amazing flowers below. It's much smaller foot print of cost then an inground system. My front system was about $100, 2 sprinklers, 1 timer, a 25' hose and poly drip line tubing. That has lasted for 2 seasons so far.

![Flowers](/assets/img/2023-08-23-hanging-pot.jpeg)

To winterize, just take the hose off and turn off the water. I cover the spouts with a winderized cover and you don't need to blow the system out. You can disconnect the timers and store them if you'd like.
