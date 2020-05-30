---
title: Automated E2E testing using protractor
date: 2015-09-15T06:00:20+00:00
author: adam.bourg@gmail.com
layout: post
permalink: /2015/09/15/automated-e2e-testing-using-protractor/
categories:
  - javascript
tags:
  - automated
  - e2e tests
  - javascript
  - tdd
  - unit tests
---
At UHG we use Protractor to test our Backbone app for automated E2E dev only regression tests. We do this as apart of an automated CI process to ensure every branch we ingrate doesn&#8217;t break existing functionaility. Today, I&#8217;m going to walk you through our setup and how you can use Protractor (an Angular tool) to test your non-Angular app. 

**Get the test runner**

I like running protractor by the CLI as much as the next guy, but you&#8217;ll want to get the grunt task runner first. This is available at: <a href="https://github.com/teerapap/grunt-protractor-runner" target="_blank">https://github.com/teerapap/grunt-protractor-runner</a>

Add the following to your grunt tasks file:

> webdriver: {

> command: &#8216;./node_modules/webdriver-manager/bin/webdriver-manager start&#8217;

> }

This will allow you to now run the protractor instance by:

  1. grunt webdriver // starts the selnium interface
  2. grunt test // runs the tests

**Configure your instance**

To our tasks file we add the following options for protractor:

> protractor: {

> options: {

> configFile: &#8216;./config/test/protractor-config.js&#8217;, // Default config file

> keepAlive: false, // If false, the grunt process stops when the test fails.

> args: {}

> },

> runner: {}

> }

Within the config file we provide a few common global helper methods. Within the config, we supply it a few options.

First, we tell it where the selenium sever is running:

> seleniumAddress: &#8216;http://127.0.0.1:4444/wd/hub&#8217;,

This is the default address location for the default instance.

Next we tell it what testing framework we want to use. Jasmine is default but we have all of our other tests written in Mocha. Mocha bundled with Chai with a <a href="https://github.com/domenic/chai-as-promised/" target="_blank">Chai As Promised plugin</a> helps us do Async tests.

> framework: &#8216;mocha&#8217;,
>
> mochaOpts: {

> timeout: 10000

> },

Then we have the following onPrepare function that loads a config file and a reusable functions file into the protractor global scope

> onPrepare: function() {

> &#8216;use strict&#8217;;
>
> // Merge in default config options for the global scope

> _.extend(global, globalConfig);
>
> // Merge the object containing all our reusable stuff into the global scope

> _.extend(global, reusableFunctions);

> }

Having things in the global scope that protractor uses; allows us to provide some easy to use default functions that make our testing efforts much easier.

A couple helpers we&#8217;ve written are:

  1. Checking for the presence of an element:

    > isPresent: function(element){

    > return browser.isElementPresent(element);

    > },

  2. We abstract the browser sleep function

    > // Allows us to pause to allow the browser to render stuff to the ui browserSleep: function(callback,time){

    > var sleepTime = time ? time : 1000;

    > if(callback){ return browser.sleep(sleepTime).then(callback()); }

    > },

  3. Inject javascript helper:

    > runScript: function(script){ return browser.executeScript(script); },

  4. Inject sinon:

    > injectSinon: function(){ browser.executeScript(&#8220;server = sinon.fakeServer.create();&#8221;); },

  5. Lastly we need to force the browser to not wait for Angular since this isn&#8217;t an Angular app:

    > disableAngularWait: function(){ browser.ignoreSynchronization = true; },

In the image above we use the standard describe / it syntax. We use a before to load the page, setup generic elements and then we fire &#8220;done():&#8221; which allows us to tell Mocha that the tests are finished.

A line like the one below allows us to check for an element to eventually be present, once the page is done loading, then notify done.

> expect(emailElement.isPresent()).to.eventually.be.true.notify(done);

We can take an element then send it new values, such as an email address field, we provide it an email address to test with:

> emailElement.sendKeys(email)

## Running the code

To run the code we trigger the grunt web driver runner:

> grunt webdriver;

To run the tests:

> grunt test;

Hopefully now you have a better understanding on how to use protractor to do automated UI testing.
