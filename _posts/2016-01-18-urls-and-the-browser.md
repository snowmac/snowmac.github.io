---
title: URLs and the browser
date: 2016-01-18T07:30:10+00:00
author: adam.bourg@gmail.com
layout: post
permalink: /2016/01/18/urls-and-the-browser/
categories:
  - deeper look
tags:
  - advanced
  - deeper look
  - uri
  - url
---
I love working with the web, there is so much to know and learn about web development. Have you ever thought about the URL? I recently learned quite a bit about the URL. The URL is composed primarily of a few things:

  1. The Scheme, which is followed by the &#8220;://&#8221;. This is typically http, https or ftp. Others such as file:// are also valid.
  2. You can also supply user name and password &#8220;user:password@&#8221;
  3. There is the host:port, which could be something like localhost:3000
  4. Then we have the path, such as /api/v1/news_feed
  5. Finally we have the query parameter, such as ?id=5&name=&#8221;adam&#8221;.
  6. The fragment identifier is the &#8220;#&#8221; in the URL. This is client side only and is not sent to the server. The fragment can be used for client routing or for client specific behavior or specifically to link to a certain location in a document.
  7. All of 1 &#8211; 5 are sent to the server. List item 6 is not sent to the server.

#6 is really interesting and new to me. I&#8217;ve never thought about a URL having two componets, client side and server side. It&#8217;s really cleaver and genius. What this raises is issues with a SPA framework however. The whole issue comes down to client vs server behavior, the &#8220;clean&#8221;, &#8220;marketing friendly&#8221; urls that don&#8217;t rely on the hash tag are always sent to the server. This is why you need mod-rewrite rules in apache. Everytime you navigate in a SPA, all of the url before the fragment identifier is sent to the server. The server has to ignore all the of these client specific urls. This adds a lot of complexitity and unneeded overhead in dealing with your SPA application. A better approach is for server invoked behavior, use the part of the URI before the fragement identifier, and for the client specific behavior, use the space after the fragment identifier.

**Resources:**

  * <a href="https://en.wikipedia.org/wiki/Uniform_Resource_Locator" target="_blank">URI</a> via Wikipedia
  * <a href="https://blog.httpwatch.com/2011/03/01/6-things-you-should-know-about-fragment-urls/" target="_blank">6 Things You Should Know About Fragment URLs </a>via HTTP watch
  * <a href="https://en.wikipedia.org/wiki/Fragment_identifier" target="_blank">Fragment identifier </a>via Wikipedia
