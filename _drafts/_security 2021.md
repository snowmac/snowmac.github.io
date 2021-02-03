---
layout: post
title: "A developers guide to common security issues and fixes"
date: 2021-02-03
categories: security code fun
---

Over the last 6 months I've been working with Penetration and Security Testers to find issues in my client's applications then fix the issues we find. We've used tools like Burp, Veracode and good ole fashioned reading code to spot some issues and get our applcations to be more secure. Today, I'm going to show you common issues we found and help you make better code decisions. 

# Being lazy will cost you

Lazy is a great way to build something really fast. Lazy gets you to the market faster. Lazy also riddles your applications with bugs, information leakage and security holes. A great, recent example of this is <a href="https://www.wired.com/story/parler-hack-data-public-posts-images-video/">Parler</a>, the community was shutdown just after the Jan 6 capitol riots. The situation here was a "hacker" created a python script that simply iterated through a set of IDs to get to almost all user information in the site. The design of Parler is simple and common, Post 1's ID is 1, Post 2 is ID 2 etc... Meaning if you know the URL structure and a single ID, you can scan the ENTIRE system to get ahold of information. This is called <a href="https://portswigger.net/web-security/access-control/idor">insecure direct object access</a>. 

A few core issues with Parler and this specific example: 

1. Parler did not secure the APIs in anyway beyond checking for an valid auth token
2. They did not rate limit their API 
3. They did not use randomly generated UUIDs 

https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html

# Storing sensitive state in the browswer 

I see this one a lot, where the developer will load something useful to global or application state in the browser, such as a cookie, local storage etc... One common issue I've seen is that the developer will load the user table into Browser memory at the time of first load; post login and stupidly sometimes pre login. This is common because all the applications we develop have a user assignment feature, but it's stupid because the developer is being lazy
