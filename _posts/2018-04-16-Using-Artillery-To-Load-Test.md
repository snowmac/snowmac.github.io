---
layout: post
title: "Using Artillery To Load Test"
date: 2018-04-16
categories: load artillery testing performance
---

Recently at work, I tasked myself with building a new test automation suite so we can start to refactor the application with low risk. One of the challenges is to ensure that performance does not decrease as we make the code higher quality.

To ensure that performance doesn't take a hit I implemented a consistent automated load testing approach using Artillery.

# What is Artillery?

Artillery is a NPM module that can perform load testing in a scripted way against any HTTP or Websocket API. You are not required to have a Node JS backend. You can use this to test any API that you own. You can check out it  [online](https://artillery.io/).

Basically it's Apache benchmark but with better tooling and in a fully scripted manner. I'm going to let you follow their setup instructions on your own over at their [docs](https://artillery.io/docs/getting-started/) while this post covers more the what and why.

# Terms and concepts

First off, it's all YAML config driven. To trigger Artillery you use artillery run path_to_file.yml. You may use javascript modules for setting things like headers or generating fake data.

* Scenarios -- This is the parent element in the YAML. Inside of this parent, you have many flows.
* Flows are the sequences that a virtual user will take when consuming your API. Maybe the first step is to authenticate to the API, then to use a JWT to make the rest of the calls. Another is each step one at a time in sequence that you want the user to take to complete some task. Like send a message or the steps in buying an item.
  * You can have more then one flow.
  * A flow can consist of just a URL and a method but can also call functions, helpers, do parsing using [Json path](http://www.prodevmentor.com/json/jsonpath/regex/2018/04/12/parsing-json.html)
  * Each flow can be named, such as the "sign user in flow", "buy an hand towel flow"

# The report

I'm borrowing a little from the [docs](https://artillery.io/docs/getting-started/#running-the-test), but here's a sample response from the artillery run.

```shell
Complete report @ 2017-08-08T17:32:36.653Z
  Scenarios launched:  300
  Scenarios completed: 300
  Requests completed:  600
  RPS sent: 18.86
  Request latency:
    min: 52.1
    max: 11005.7
    median: 408.2
    p95: 1727.4
    p99: 3144
  Scenario duration:
    min: 295
    max: 11127
    median: 743.1
    p95: 3026.5
    p99: 4632.2
  Scenario counts:
    0: 300 (100%)
  Codes:
    200: 300
    302: 300
```

* Scenarios launched is the number of virtual users created, these users choose from which flow to use
* Scenarios completed is the number of virtual users that completed their scenarios
* Requests completed is the number of requests that have returned a response
* RPS sent is the average number of requests per second completed
* Request latency and Scenario duration are in milliseconds, and p95 and p99 values are the 95th and 99th percentile values (a request latency p99 value of 500 ms means that 99 out of 100 requests took 500ms or less to complete).

**Above defs are taken but edited from the docs**

# What can we do with this information?

Well, when we load test we're given the ability to determine how the API is performing which informs us to whether or not our change set is a good for performance or not. It also helps us make decisions on what technology to use and our architecture.

Additionally, we could run New Relic at the same time and sample our memory, CPU and database performance during the load test. This will give us deep insight to our performance while under simulated load.

# I need to write some custom headers and do some fancy stuff

Ok Mr. fancy pants. I had the same problem, this is YML, how am I ever going to be able to inject headers and do all the magic that I need to do to be able to make a call? I have a solution for you.

The docs are a little [obtuse](https://artillery.io/docs/http-reference/#loading-custom-js-code) on this one, but you need to call a 'processor' in the config section. All the processor does is load the file, importing it's module exports into the local context.

Once you import that file, you can write functions to be called on two lifecycle hooks: ```beforeRequest``` and ```afterRequest```.

Before Request is the most helpful as it gives you 4 params:

```javascript
function myBeforeRequestHandler(requestParams, context, eventEmitter, next) {
}
```

* requestParams (headers, body, cookies)
* context is the virtual user's context
* eventEmitter can be used to communicate with Artillery
* next is the callback which must be called for the scenario to continue; it takes no arguments

What is nice about this is that you can change the requestParams, which includes the body, the method, the headers etc... This is really helpful if you have to load an OAuth token or something similar before moving on with the load test.

# Building complex workflows

The flow is really powerful. Think of it as all the steps in order for the transaction to be completed. Such as purchasing an item or making a comment. I'll give you an example of how to do a purchase call:

```yaml
- name: "Purchasing an item"
flow:
  - get:
    url: "/store/laptops"
    beforeRequest: "SignUserInMethod"
    capture:
      json: "$.data[0].laptopId"
      as: "ItemID"
  - post:
    url: "store/addToCart/{{ ItemID }}"
    capture:
      json: "$.data.cartID"
      as: "cartID"
  - post:
    url: "store/checkout/{{ CartID }}"
```

### What are we doing here?
Well, first we get a index listing of all laptops, then we take the first one available set it to be a variable ```ItemID``` then use that in the next request which happens to be POST to add the item to the cart. Once that's done we store the Cart ID and use that to checkout.

# How does this roll up?

The basic config looks similar to this:

```yaml
  config:
    target: "http://localhost:3001/"
    phases:
      - duration: 60
        arrivalRate: 10
    processor: "./PathToMyCustomJSFile"
  scenarios:
    - name: "flow 1 example"
      flow:
        - get:
          url: '/index'
    - name: 'flow 2 example'
      flow:
        - get:
          url: "/store/laptops"
          beforeRequest: "SignUserInMethod"
          capture:
            json: "$.data[0].laptopId"
            as: "ItemID"
        - post:
          url: "store/addToCart/{{ ItemID }}"
          capture:
            json: "$.data.cartID"
            as: "cartID"
```

**Lets explain some things:**

There is only 1 config, processor and scenarios key. The name comes before a flow, allowing a human readable string such that it can be clear what you're testing. The flow is the sequence of API calls the virtual user makes. You can add a weight to each flow to ensure one flow gets called more then others.

The duration is how long you want the test to run in seconds, in our case its 60 seconds or 1 minute. The arrival rate is how often a new virtual user should hit the API per second. Given 10 per second, we're testing 600 virtual users split between these flows.

More items in a single flow probably better represent how a single user will consume your api. If each flow is only 1 API call deep, it's probably not enough to get a accurate representation of what the load looks like. A single user will probably make many API calls.

# Closing thoughts

Building a complex set of tests for each REST resource would help you load test your software to ensure that no matter the demand you can scale without significant risk. It also gives you the advantage of understanding your performance bottlenecks.

Using New Relic with load testing will give you insight into how your application is performing while under heavy load, it will show you the slow API calls, the slow database calls and help you kill performance headaches.
