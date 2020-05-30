---
title: Secure credential storage
date: 2015-08-11T07:30:44+00:00
author: adam.bourg@gmail.com
layout: post
permalink: /2015/08/11/secure-credential-storage/
categories:
  - hipaa
tags:
  - 12 factor
  - devops
  - factor 12
  - phi
  - security
---
A couple of weeks I reviewed a pull request from one of our consultants. It contained a set of credentials to authenticate to a health API which could obtain production PHI. That information was stored in source control in plain text.

After escalation of the issue we got the it resolved and we&#8217;re now loading the passwords through a secure system. This got me thinking about how other people approach security.

Storing credentials in source control is a bad idea, especially if it can obtain PHI or user information. So you need to store a set of credentials or keys to access an API or service but you shouldn&#8217;t store it in source control. Why not?

  * Anyone with access to your source can see it.
  * Any disgruntled employee can see it who has access to the source.
  * If your source is publicly available, they could see it
  * if your source is stored on an unencrypted device, people could obtain the source and the credentials.
  * Social engineering could occur for a team mate to send the credentials from the source to an attacker.

Some of these might be far flung scenarios, but hackers have a way of getting what they want. Anthem was hacked earlier this year (In February 2015) by a social engineering attack.

But I need to access the service! You have some choices:

  1. Encrypt the credentials and store it in a file in source control.
      * Ensure that the decryption key is not stored in source control. This is more secure because it allows the users of the app to do their work but it prevents anyone with access to the source code total access to the credentials. However depending on the encryption and how much time they have it can be broken.
  2. Configure the credentials to be stored in a config file that gets loaded into an system environment variable when the system boots which is available to the source code.
      * Downside is if on a shared host it could expose the information to other system users.
  3. Load the credentials into a secure key management system.
      * Options include SafeNet and Amazon&#8217;s CloudHSM.
          * Cons can be cost, access and integration. For a Rails project we worked on we have to build a custom gem to integrate with SafeNet and the approval process took almost 8 months.
  4. Load the credentials into a local keychain
      * If the local system has something like the Mac&#8217;s Keychain, storing it there might be a way to ensure you can use the credentials without risking data breach.

I personally choose SafeNet whenever possible. I think it&#8217;s the most robust and it ensures that the system won&#8217;t get hacked. If someone had access to the code, but were not authorized to access SafeNet, the keys would not be available to the attacker.
