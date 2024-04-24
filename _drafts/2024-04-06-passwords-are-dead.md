---
layout: post
title: "Passwords are dead"
date: 2024-04-06
categories: passwords
---

Passwords are dead. Well, not really, but I lothe and hate passwords with servere distain. As an engineer they're easy to implement, difficult to get right and flawed at the human level due to human ignorance, laziness or stupidty. Passwords need to no longer exist. What then can replace passwords? Identity verification and authorizon keys.

Lets break the idea down further. Identity verification exist by verifying you are who you say you are, 2 factor style. Send me a text and/or an email. I click the "magic" link and I'm now signed into your application. The link is now forever expired. How do I get another session? You send me a link. The authorization key, like a giant password should be a physical hardware key, 256 bit or larger. You plugin the key, verify your identity and you are into the system. Just like at my bank when I go to access my safe deposit box, I show my drivers license and use my physical key to sign into the deposit box. Key + identity = massive safety. Add logging and you've solved complex security.

It's time developers stop using Passwords. Identity verification for Facebook, fitness trackers, forums and other non essential sources of information, should no longer use passwords. Banks, investment accounts etc... should ship you a physical USB key that they assign a token generator based on private and public keys that combined with identity verification gets you signed into the system. Don't have the key? You can't get in, you have to call the support number or visit a local branch.
