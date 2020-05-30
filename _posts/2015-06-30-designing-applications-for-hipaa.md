---
id: 10
title: Designing Applications for HIPAA
date: 2015-06-30T21:47:10+00:00
author: adam.bourg@gmail.com
layout: post
guid: http://www.adambourg.com/?p=10
permalink: /2015/06/30/designing-applications-for-hipaa/
categories:
  - hipaa
  - web applications
tags:
  - compliance
  - hipaa
  - spa
  - web
  - web applications
---
Welcome to my blog. I’m Adam. I’m a Senior Software Engineer for a health insurance company. Me and my team are designing the next generation web applications that will transform the healthcare industry. Currently we’re building a call center application in Javascript.

Today we’re going to be discussing HIPAA compliance and concerns when building web applications.

**HIPAA basics**

HIPAA is the Health Insurance Portability and Accountability Act. Title II of the law focuses on digitalization of healthcare information. It puts in place legal accountability for healthcare providers and how they handle your PHI (Protected Health Information).

Within HIPAA you have various set of rules, rules for how you handle data, rules for who handles data, rules for transaction standards you must adhere to as well as security standards.

Under the privacy rules, if you are a covered entity such as a hospital or doctor you can transmit a patient’s PHI without their consent for their treatment to other covered entities.  You cannot disclose their PHI without their consent to non-covered entities like their brother or 3rd party companies. You however can be forced by law to disclose to law enforcement.

Under HIPAA some of the most important rules to abide by are the administration rules. It primarily focuses on:

  1. Who has access to data and physical access to where it’s stored
  2. Who should have access
  3. Placing safeguards in to prevent unauthorized access
  4. Reporting when unauthorized access occurs

The  general rule of thumb from a technical perspective is we protect data when it is in flight and at rest. Production machines are locked down to specific users, all actions and modifications are recorded. Deployments to prod are locked down and regulated, documented and controlled.

On the administrative side, we have security officer for handling the documentation of how we’re in compliance with HIPAA. We have contingencies in place for emergencies. We identify people who have access to PHI. We have internal audits to ensure compliance. We have a written policy and strategy for when there are breaches in security and data is leaked.

**PHI: What is PHI?**

Well, PHI stands for Protected Health Information. This is identifying information about a medical consumer, it includes things like your data of birth, address, phone numbers, fax numbers, social security numbers, serial / member numbers and basically anything that could identify a person including pictures. PHI is the data that identifies a consumer of medical services.

**How does HIPAA affect developers?**

HIPAA affects you if you’re interacting with an API that serves healthcare data or you store healthcare data. At the insurance company I work at we build API’s, we consume API’s and we store a lot of PHI.

There are a few main states of concern when dealing with PHI from an application perspective:

  1. Who has access to data and what safeguards are in place when people access this data?
  2. How secure is the data as it is in rest? (stored on disk or memory)
  3. How secure is the data in flight? (Transmitting over the wire)

**Who has access to data and what safeguards are in place when people access this data?**

In our call center application, a customer calls in, we enter their information and we POST it over HTTPS to a server to store their information. The agent, when is finished with the call, hangs up, and has to record when they accessed the member’s data and why. This creates an accountability trail.

The other general concern we have is when we do production deployments where we could be affecting live data. We have to document, who’s doing the deployment, what records they will be accessing, what systems they will be accessing and what commands they will run. This check and balance ensures that we have the accountability to ensure our customer’s data is secure. This is important because when there is a breach, you need to report this to the customers whose data has been affected and the public.

**How secure is the data as it is in rest? (stored on disk or memory)**

This is an interesting challenge from the perspective of an application because you can have multiple subsystems that store various PHI data. You can have an API that caches its queries from a database, you can a database store the data and you can have a web front end that use HTML5 local storage to cache some PHI to an agent’s or consumer’s computer. If you persist PHI in cookies, you must encrypt them to ensure unauthorized persons do not have access.

In the case of the database store, it’s recommended you either encrypt the data using AES encryption. You can encrypt the fields, or some database systems allow you to encrypt the tables (such as Postgres). Beyond that, you should encrypt the hard drives so that if someone were to steal a drive, it would be irrecoverable.

If you do not need read access to the data, it would be better to hash the data and encrypt the file system. The approach we’ve used is to take a composite value of their social security number, date of birth, full name and some salt. We store the hashed result and the salt (random for each row) in the database with a primary key. This allows us to lookup things like how much health insurance plans cost, specific to that user without worrying about the two way venerability of their data.

If you store any of their data in a flat file, it&#8217;s recommended to use something like GPG to encrypt that file, then hash or encrypt each field if possible.

**Beyond the application, what can we do to secure data at rest?**

Really glad you asked this question! There are a lot of things that you can do. The best option is to encrypt the hard drives. Mac, Windows and Linux support some level of encryption on the hard drive to secure the data when the system is in a powered off state.

When disposing of hard drives, be sure to wipe them then physically destroy the devices.

**How secure is the data in flight? (Transmitting over the wire)**

When transmitting the data it must also be secure. Send the data over HTTPS. Beyond this besure to use a system like OAUTH to ensure that users or applications have privileges to the data they are accessing.

Another option is you could encrypt the data, send it over HTTPS then decrypt client side.

**How do I know if there’s a breach?**

Normalcy in your system isn’t necessarily a good indicator of no breaches in your system. To detect a breach, it requires a really well defined audit trail. You need to have server logs, you need them backed up. You need to have logs of all system activity, both on the servers and the application activity. You need to restrict access to production to limited accounts with limited accesses / commands. You can use a tool like Protect Wise to record network activity.

When querying the data both from the database and through your app, you should record who is querying for what. You need to have regularly occurring audits to ensure breaches aren’t occurring.

**Summary**

HIPAA primarily deals in the processes around how you handle data and breaches. It doesn’t regulate the technical approaches you must use, other than the generics: secure in fight and at rest. Beyond that, it’s up to you to determine what is best for your organization and application. My advice, start small.

Field encryption and HTTPS are really great places to start, then explore other options. You want your app to be HIPAA compliant and the ability to move fast. The general questions to ask yourself is (from an engineering perspective):

  1. Is my data secure at rest? Server side? Client side?
  2. Is my data secure in flight?

P.S.

_This is my first major blog post, please leave your feedback in the comments below._
