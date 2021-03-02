---
layout: post
title: "Using plain javascript to espace HTML"
date: 2021-03-02
categories: javascript dom frontend
---

At work I've spent the last 6 months working on security issues. From jQuery updates to React, Angular and bootstrap and every possible framework in between. I'm going to show you a little trick you can use from the DOM to sanitize output without bringing in a library. 

This is the messy jQuery code I'm working to fix: 

```javascript
  $.ajaxEx({
    url: __GLOBAL_SCOPE__.APIRoot + "/super/createccUser",
    method: "post",
    data: param,
    success: function (res) {
        if (res.code === 0) {
        $('#message #messageText').html('').append('<p>Create user success!</p>');
        userManagement.resetModal();
        $('#createUser').modal('hide');
        $('#message').modal();
        } else {
        $('#message #messageText').html('').append('<p>Error:' +res.msg+ '</p>');
        $('#message').modal();
        console.error(res);
        }
    },
    error: function (err) {
        $('#message #messageText').html('').append('<p>Error:' + err + '</p>');
        $('#message').modal();
        console.error(err);
    }
});
```

Veracode is complaining about the response in the two functions, the `res.msg` and `err` variables because they could contain HTML and inject a Cross Site Scripting bug (XSS). I could do something like use Regex, set something on the global scope or import something like HTML Escape Goat. Or I could use the dom method: `document.createTextNode`. 

Being a through developer, I figured out that if you did something like `document.createTextNode("<h1>jQuery is stupid</h1>")` will give you the string encoding with tags of jQuery is stupid. Just what I wanted; so a minor change to the code and veracode is no longer complaining. Doc create text node will return a string, therefore you can call it inline:  

```javascript
  $.ajaxEx({
    url: __GLOBAL_SCOPE__.APIRoot + "/super/createccUser",
    method: "post",
    data: param,
    success: function (res) {
        if (res.code === 0) {
        $('#message #messageText').html('').append('<p>Create user success!</p>');
        userManagement.resetModal();
        $('#createUser').modal('hide');
        $('#message').modal();
        } else {
        $('#message #messageText').html('').append('<p>Error:' +document.createTextNode(res.msg)+ '</p>');
        $('#message').modal();
        console.error(res);
        }
    },
    error: function (err) {
        $('#message #messageText').html('').append('<p>Error:' + document.createTextNode(err) + '</p>');
        $('#message').modal();
        console.error(err);
    }
});
```

Why does it work? Well, according to <a href="https://developer.mozilla.org/en-US/docs/Web/API/Document/createTextNode">Mozzila</a>, it's used to escape HTML elements. `Creates a new Text node. This method can be used to escape HTML characters.` It's supported since Chrome/Safari/Firefox 1, IE 5 and Opera 7. Push that easy button! 
