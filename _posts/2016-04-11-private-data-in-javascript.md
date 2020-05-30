---
title: Private Data in Javascript
date: 2016-04-11T15:57:38+00:00
author: adam.bourg@gmail.com
layout: post
permalink: /2016/04/11/private-data-in-javascript/
categories:
  - deeper look
  - javascript
---
One of the things that I feel is really missing from the JavaScript programming language is the option of private data and private behavior (methods) to an object. I never could get data that an outside caller couldn&#8217;t see. That is until I discovered the JavaScript closure.

A closure is typically a function. You can control scope, by returning an object containing data and public instances. What does one look like?

> (function(){
>
> })();

On line 1, we declare an anonymous function and on line 3, we end it and then immediately invoke it. We don&#8217;t return any data, we return undefined by default. What&#8217;s interesting is that you can pass arguments so that the variables that you use within the scope are local:

> (function($,_){
>
> })($, _);

As you can see we&#8217;re now passing in a jQuery block and an underscore block, no longer do they have to be globals.

To expose data you can return specific data or an object:

> (function($,_){

> var myPrivateData = &#8220;randomSocialSecurityNumber&#8221;;
>
> return {

> time: Date.now(),

> socialSecurityNumber: myPrivateData

> }

> })($,_);

Here&#8217;s a full example with public and private data:

> var App = window.App; // get a global

> var id = submissionID;
>
> var payRoll = (function($,_, App, id){

> var user = App.collection.model(id);

> var timeSheet = App.collection.timeSheets.model({userid: id});
>
> var grossPay = (function(timesheet){

> return timesheet.rate * timesheet.hours;

> })(timeSheet);
>
> var takeHomeRate = (function(user){

> return 1 &#8211; user.taxRate;

> })(user);
>
> return {

> hourlyRate: timeSheet.rate,

> hoursWorked: timeSheet.hours,

> grossPay: grossPay,

> netPay: grossPay * takeHomeRate,

> id: user.id,

> firstName: user.firstName,

> lastName: user.lastName,

> };
>
> })($, _, App, id);

So for our payroll object, if we wanted to access the takeHomeRate, we can&#8217;t because it&#8217;s completely private. We can&#8217;t say payRoll.takeHomeRate. But we can say payRoll.grossPay, because it is data we expose by returning it. If we don&#8217;t return it, won&#8217;t be public. Which means that now we can have an assortment of private attributes to an object that has no exposure, creating a contract by which you can modify the internal structure of JavaScript objects without changing the contract and breaking future users.
