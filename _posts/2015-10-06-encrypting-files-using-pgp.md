---
title: Encrypting files using PGP
date: 2015-10-06T07:00:10+00:00
author: adam.bourg@gmail.com
layout: post
permalink: /2015/10/06/encrypting-files-using-pgp/
categories:
  - hipaa
  - phi
tags:
  - encryption
---
PGP is a encryption tool I use to encrypt and decrypt files containing sensitive data.

We use GPG to decrypt PGP files as a part of our ETL process. GPG Wiki: [http://en.wikipedia.org/wiki/GNU\_Privacy\_Guard](http://en.wikipedia.org/wiki/GNU_Privacy_Guard)

## Requirements

GPG is required to be installed on any system that decrypts PGP files. There are many binaries available for download depending on your OS at: <a href="https://www.gnupg.org/download/" target="_blank">https://www.gnupg.org/download/</a>.

To install on a Mac, we highly recommend using Homebrew.

> brew doctor

> brew update

> brew install -v gpg

Windows users: <a href="http://www.gpg4win.org/" target="_blank">http://www.gpg4win.org/</a>

## Importing existing keys

> gpg &#8211;import *

This will import both keys

## Creating keys

1. From the command line run the following commands:

2. &#8216;gpg &#8211;gen-key&#8217;

You will be taken through a series of prompts:

1. &#8216;Please select what kind of key you want:&#8217;, enter the value 1 to select &#8216;RSA and RSA (default)&#8217;

2. &#8216;RSA keys may be between 1024 and 4096 bits long. What keysize do you want?&#8217;: Press enter to go with the default, typically 2048 which is fine. Longer is more secure.

3. &#8216;Please specify how long the key should be valid&#8217;:

options are:

0 = key does not expire

<n> = key expires in n days

<n>w = key expires in n weeks

<n>m = key expires in n months

<n>y = key expires in n years

For exipres in 3 weeks use:

3w

It will give you a date and ask you if this is correct, enter &#8216;y&#8217; if it is, &#8216;n&#8217; if it is not

4. &#8216;You need a user ID to identify your key; the software constructs the user ID from the Real Name, Comment and Email Address in this form:&#8217;

Since PGP is used to encrypt emails and not typically files, you need to enter a name, comment and email to sign this document with.

For the &#8216;Real name:&#8217; I&#8217;m going to use the project&#8217;s name &#8216;Private Exchange&#8217;

For the &#8216;Email address:&#8217; I&#8217;m going to use my own, &#8216;adam.bourg@blah.com&#8217;

For comment, I&#8217;m leaving it blank

Next prompt:

&#8220;You selected this USER-ID: &#8220;Private Project <adam.bourg@blah.com>&#8221;

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit?&#8221;

Enter O to say okay.

5. &#8216;You need a Passphrase to protect your secret key. Enter passphrase:&#8217; This is a password used to unlock the file with the private key. I&#8217;m going to use the phrase &#8216;purple\_flowers\_blue\_sky\_2015&#8242;

You&#8217;ll be asked to repeat the same phrase. You need to save this thing, random is better and long is better. If you lose the key or the phrase, you&#8217;re screwed, you can&#8217;t decrypt the file.

6. You should see out put similar to:

We need to generate a lot of random bytes. It is a good idea to perform

some other action (type on the keyboard, move the mouse, utilize the

disks) during the prime generation; this gives the random number

generator a better chance to gain enough entropy.

.+++++

..+++++

We need to generate a lot of random bytes. It is a good idea to perform

some other action (type on the keyboard, move the mouse, utilize the

disks) during the prime generation; this gives the random number

generator a better chance to gain enough entropy.

.+++++

&#8230;&#8230;&#8230;&#8230;.+++++

gpg: key 55FB8C3D marked as ultimately trusted

public and secret key created and signed.

gpg: checking the trustdb

gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model

gpg: depth: 0 valid: 4 signed: 0 trust: 0-, 0q, 0n, 0m, 0f, 4u

gpg: next trustdb check due at 2015-03-02

pub 2048R/55FB8C3D 2015-02-27 [expires: 2015-03-02]

Key fingerprint = 6F4A D6CF EE9B 7101 579E 33BE 3431 A309 55FB 8C3D

uid Private Exchange <adam.bourg@blah.com>

sub 2048R/EB4B2DDB 2015-02-27 [expires: 2015-03-02]&#8217;

3. This will generate two keys that are saved to your pgp key chain.

## Encrypting a file

Now that you have your keys, lets say you have a file called &#8220;major\_risk\_data.csv&#8221; and you want to encrypt that file.

Using the command line:

1. cd into the directory where the file is stored

2. Encryption command explained:

gpg &#8211;output {where\_you\_want\_it\_saved} &#8211;encrypt &#8211;recipient {what\_is\_the\_email\_of\_the\_user} {path\_to\_file\_to\_be_encrypted}

{where\_you\_want\_it\_saved}: whats the path you want to save the file to

{what\_is\_the\_email\_of\_the\_user}: the user you entered for the key, within the pgp config this is stored as the &#8217;email&#8217; field.

{path\_to\_file\_to\_be_encrypted}: the path to the file to be encrypted

3. Example using repo keys:

gpg &#8211;output ./major\_risk\_data.pgp &#8211;encrypt &#8211;recipient foo@bar.com ./major\_risk\_data.csv

it may prompt you saying:

gpg: AEFA524B: There is no assurance this key belongs to the named user

pub 2048R/AEFA524B 2014-11-07 foo@bar.com

Primary key fingerprint: 4D92 72E5 8CC8 E1EB CA11 544A 07B3 E105 AEFA 524B

It is NOT certain that the key belongs to the person named

in the user ID. If you \*really\* know what you are doing,

you may answer the next question with yes.

Use this key anyway? (y/N)

For testing purpose this is fine, just say yes (y).

4. Now you should see a pgp file named &#8216;phi.pgp&#8217; in your current directory.

## Decrypting a file

Files to be decrypted must have the extension &#8220;.pgp&#8221; at least for the ingest process, but really for the tool itself it can have any extension.

Using the command line:

1. cd into the directory where the file is stored

2. Decryption command explained:

gpg &#8211;output {where\_you\_want\_it\_saved} &#8211;decrypt {encrypted_file}

{where\_you\_want\_it\_saved}: path to where you want the decrypted file to be saved

{encrypted_file}: path to encrypted file

3. Example using repo keys:

gpg &#8211;output ./phi_decrypted.csv &#8211;decrypt ./phi.pgp

It will output something similar to:

You need a passphrase to unlock the secret key for

user: &#8220;foo@bar.com&#8221;

2048-bit RSA key, ID AEFA524B, created 2014-11-07

Enter passphrase:

You&#8217;ll enter the passphrase from the config file or from the passphrase that you gave to the keys when you created them.
