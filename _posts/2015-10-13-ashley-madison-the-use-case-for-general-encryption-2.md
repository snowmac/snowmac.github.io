---
title: 'Ashley Madison: The use case for general encryption'
date: 2015-10-13T07:18:30+00:00
author: adam.bourg@gmail.com
layout: post
permalink: /2015/10/13/ashley-madison-the-use-case-for-general-encryption-2/
categories:
  - encryption
  - security
---
Encryption really isn&#8217;t the sexiest topic, certainly not as interesting or thrilling as something like Ashley Madison, a site that promises you discrete encounters no matter your marital status.

Their entire premise is &#8220;Life is short. Have an affair!&#8221;. This presents a general use case that we as web developers must look at more closely. Encryption for the web isn&#8217;t just for passwords any more. It really should be about EVERYTHING else, because the &#8220;devil is in the details&#8221;.

## What data was leaked?

Well according to <a href="http://www.wired.com/2015/08/ashley-madison-hackers-release-even-bigger-batch-data/" target="_blank">Wired Magazine</a> we know that the hackers released 36 million records of the following pieces of data:

  * Names
  * Addresses
  * Last 4 digits of credit card numbers
  * Billing information
  * Transaction History

In the world of Healthcare IT all of this information would be considered protected information and subject to protection in flight and at rest. But in the general web development community encrypting and securing the row by row data is mundane. I just want to build cool apps really fast MOFO!

## How do we secure the data?

Glad you asked sammy, there are a few of options.

1. Secure the data row by row using encryption at the database layer.

This solution is great because you offload the task to encrypting and decrypting the data to the database. You would probably need to access the data using a stored procedure or something similar as there are two functions: one for decrypting and the other encrypting.

In MySQL 5.7 they offer support for AES encryption and decryption. (Cite 2)

Postgres supports PGP, DES and AES right out of the box. See more at their docs page. <a href="http://dev.mysql.com/doc/refman/5.7/en/encryption-functions.html" target="_blank">Mysql Encryption Doc Page</a> <a href="http://www.postgresql.org/docs/9.4/static/pgcrypto.html" target="_blank">Postgres Encryption Doc Page</a>

2. Encrypt the data at the application level. An Gem Hot Like sauce comes to mind.

### Rails options for encrypting data

In Rails there are a couple of options to encrypt the data. The main way to encrypt the data using a row level, model method using a gem such as <a href="https://github.com/jstin/hot_like_sauce" target="_blank">Hot Like Sauce</a> or <a href="https://github.com/attr-encrypted/attr_encrypted" target="_blank">attr_encrytped</a>. There&#8217;s a really good <a href="https://mikecoutermarsh.com/rails-keeping-your-users-data-safe/" target="_blank">article</a> by Mike Countermarsh about this topic.

### Javascript options for encrypting data

There aren&#8217;t very many options to encrypt data for Node or MongoDB. MongoDB currently doesn&#8217;t support encryption of the data expect through application or file system level encryption.

With Node you can encrypt the data before you save it into the database like you would in a Rails application. Two tools come to mind: <a href="https://www.npmjs.com/package/node-cryptojs-aes" target="_blank">Node-cryptojs-aes </a>and <a href="https://www.npmjs.com/package/bcrypt-nodejs" target="_blank">bcrypt-nodejs</a>.

### File system encryption

Now that you&#8217;ve covered the data at rest, the other thing you might consider is how you encrypt the data when its stored completely cold, on the file system. There are a number of options, such as Filevault which comes with the mac or bitlocker which comes with Windows. Even with Ubuntu you can create an encrypted home directory.

### Handling data in flight

Typically you will want to deliver the data over HTTPS. You could go even further and custom encrypt the data before you fire it away to the customer, and decrypt on the client. This would ensure that only authorized users could view it with their keys and prevent a man in the middle attack.

&nbsp;
