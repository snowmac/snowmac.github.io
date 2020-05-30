---
title: Scrum is the new waterfall
date: 2015-11-10T11:00:04+00:00
author: adam.bourg@gmail.com
layout: post
permalink: /2015/11/10/scrum-is-the-new-waterfall/
categories:
  - career
  - productivity
tags:
  - agile
---
Scrum while great in theory is in practice a really flawed process of creating software. Scrum is iterative waterfall. Scrum is process hell. Saying this, may get me shunned and kicked out of the Agile club. But I really believe that the bane of our industry is the process management called &#8220;Scrum&#8221;.

## Scrum is Agile

No it&#8217;s not Agile. Scrum is anti Agile. It calls itself a Agile approach or methodology but if you read the <a href="http://www.agilemanifesto.org/" target="_blank">Agile manifesto</a> scrum by that definition is never going to be Agile. The process of Agile is the prioritizes people and interactions over processes and tools.

Scrum has many &#8220;ceremonies&#8221;, it feels like going to grandma&#8217;s old church services where the people repeat what the &#8220;Scrum master&#8221; says, listen to the ideas put forth in &#8220;Sprint Planning&#8221;, &#8220;Grooming&#8221;, &#8220;Stand up&#8221; etc.. It&#8217;s boring, its old, it leads to pointless meetings run by people who don&#8217;t write software, who don&#8217;t understand the technical process behind writing software and don&#8217;t always care.

Adhere to the sprint commitment, even if you have to work over time. You committed so you have to deliver. Since when did a human ever estimate something accurately. We can&#8217;t even do this when building sky scrapers, let alone a  5 million dollar software project.

## How to be Agile

Accept that Agile is about people first and foremost. What will move you quickest to the goal? Be pragmatic. Don&#8217;t waste time on pointless meetings like planning or grooming if that&#8217;s not what will allow us to move faster.

Use standups for what they&#8217;re designed for, they&#8217;re not for updating your status to your managers. It&#8217;s about quickly getting the team unblocked and moving fast. Stop meeting everyday at 9 am. Start meeting many times a day, if there&#8217;s a blocker, get the people you need in a room, stand up and unblock the thing you are working on.

Agile is about moving fast, building working software today and delivering with changing requirements. Scrum can&#8217;t change without process during the sprint cycle, this inhibits your ability to change and move faster. What if yesterday the requirements were X and today now they&#8217;re X and Y? What if you can deliver both today rather then next sprint? Doing it today might be better then next sprint .

## Move faster

You need to write tests. Does the UI render and do its thing correctly in all happy paths? What happens when the data is bad? Test your APIs, do they contain the right contracts, ensure that they are returning the correctly formatted and designed data and that they contain correct data. Test performance and security.

Can you ship what&#8217;s on Master right now? If not you have a lot of work to do. Master should always be ready to go to production. If you can&#8217;t, you&#8217;re not Agile.

Writing tests reduces risk, If you refactor or redesign you can ensure that the system won&#8217;t break.

## Screw unit tests, test the contracts

I bet you 90% of the time your code isn&#8217;t doing something totally unique like calculating the cost of a family of 5 with disabilities and all kinds of heart issues. Test where it makes sense, unit tests can be great but they tightly couple your tests to your code, making it really fragile and anti Agile.

This is where contract testing comes in. Test the contracts between classes, what is the public interface? Ensure this always does something sane even with bad data. Test the API contracts! Ensure the API returns valid data, validate with a JSON schema or an XML WISDAL or whatever schema you can get for your API.

Test UI contracts. Whats the main success scenario? What is the common path, Test functionality, not design or placement.

## If you have to, use Kanban

I think most processes are a waste of time expect Kanban. Have a few simple columns:

  * Undefined &#8212; Someone needs to add details
  * Defined &#8212; We think we have enough details to work on it
  * Working on it &#8212; A developer is working on it
  * Done &#8212; Its done and ready for approval from the creator
  * Approved &#8212; this isn&#8217;t a column but a state, when it&#8217;s done, it&#8217;s off the board.

A card doesn&#8217;t have enough details! So ship it back to undefined or get out your chair and talk to the person who wrote it!

It has no task hours: Humans suck at estimating. Instead log actual hours if this is a important metric (ex: consulting company).
