---
title: Static site hosting using Amazon S3
date: 2015-08-25T07:00:48+00:00
author: adam.bourg@gmail.com
layout: post
permalink: /2015/08/25/static-site-hosting-using-amazon-s3/
categories:
  - aws
tags:
  - amazon
  - devops
  - was
---
My wife and I sell gluten free cookies at local coffee-shops and farmers markets. We love this business, it&#8217;s a lot of fun and time to spend together. We recently needed a website as we&#8217;re starting to approach local grocery stores and they need to read about our product.

Hosting can be expensive and a pain in the butt. The last thing I wanted was to have a system where I had to worry about backups or up time. If it weren&#8217;t for the friendly UI of WordPress, this site would be on there too. S3 is highly available and you only pay for the bandwidth used. The most I&#8217;ve ever paid in a month is about $10.00.

We use it for static website hosting. Our template was made by some team in India (<a href="http://www.chewyandgooeycookies.com" target="_blank">www.chewyandgooeycookies.com</a>) and we bought it through ThemeForest. We just chucked in our content, threw it up on S3 and we&#8217;re done.

**Here&#8217;s how you create a static site on S3: **

1. Sign up for an AWS account: <a href="http://www.Amazon.com/aws/" target="_blank">www.Amazon.com/aws/</a>

2. Once in the console, go to &#8220;S3&#8221;, then click the big blue button that says &#8220;Create Bucket&#8221;. Name this: www.yourdomain.com. Save this.

3. Then click &#8220;Create Bucket&#8221; again, name this: yourdomain.com. Save it.

4. Once you&#8217;ve got the buckets created, right click on the www bucket, go to properties and click on &#8220;Static Site Hosting&#8221;, set this to be the &#8220;Enable Website Hosting&#8221; property. Specific the index document (typically index.html). Then save.

5. Once you&#8217;ve done that go to the non www bucket, go to properties and then &#8220;Static Site Hosting&#8221;. Select the redirect all option, and point it to www.yourdomain.com. Then save.

&nbsp;

6. Go into the www bucket, select all items, right click and select &#8220;Make Public&#8221;. Agree to the warning and click save. This allows the visitors of your site to see your content.

This gives you a working website, what do you do when you need that www.yourdomain.com to work? There&#8217;s an extra couple of steps there. Basically you create a Route 53 domain configuration through the AWS console and setup the DNS to point to the S3 bucket. Then you configure on the domain name side of things to point to the Amazon DNS servers. More information about this can be found by reading Amazon&#8217;s documentation on using <a href="http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html" target="_blank">custom domain names.</a>
