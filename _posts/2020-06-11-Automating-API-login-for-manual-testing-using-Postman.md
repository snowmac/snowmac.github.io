---
layout: post
title: "Automating API login for manual testing using Postman"
date: 2020-06-11
categories: 
---

[Postman]() is a very powerful tool for API development. If you're like most developers I know, you use it as a CURL with folders. That is until now. Postman can do a lot more then help you stay organized. You can use Postman to build automated and manual tests, you can also use variables in URLs, headers and other locations to facilitate easy API testing. Today we're going to show you how to make a reusable login method that will allow you to fire a request, automatically log into the API, then shove the JWT automatically into a variable to be used by a header. Why is this important? 

Well if I want to test a new private API, I have to auth to the API first. I could manually call the login API, then copy values into the header then call my API; but what if I want a button push to login? That's what we're going to do. 

# The how


Basic setup 

In Postman: 
1. Create a new request
2. Click on the headers tab then set `Content-Type: application/json`
3. The click on the body tab and provide your auth JSON, mine looks like `{"email": "adam.bourg@gmail.com", "password": "mypassword"}`

This will auth you to the API. There is one final step however, you need to go to the 'Tests' tab and paste in the following code:

```javascript
pm.test("ensure API replied all happy", function () {
    pm.response.to.not.be.error;
});

pm.test("set local env vars", function () {
    var data = pm.response.json();
    var sessionId = data.data.sessionId;
    var token = 'jwt:' + data.data.token;
    var words = CryptoJS.enc.Utf8.parse(token);
    var base64 = CryptoJS.enc.Base64.stringify(words);
    
    pm.environment.set("SESSIONID", sessionId);
    pm.environment.set("Authorization", base64);
});
```
What's nice about this is that all of the tests are javascript code (it is an electron app after all). The line `pm.environment.set` is the magic. This strips the jwt from our response, sets it as an ENV variable to the post man and will allow us to use it within our post man environment as a variable. 

# How to use the token in API requests

The final step is to go to a request you need the header value set, navigate to Authorization. Once there, select "Type" to be your token type for us it is "Bearer Token". Then for the token, call the variable `{{Authorization}}`. Once you've fired the login API, you can now go to any request that has `Authorization` and run that request without any manual work. 

![Auth token](/assets/img/06112020_postman_auto_login.PNG)