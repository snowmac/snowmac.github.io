---
layout: post
title: "Lets explore console log"
date: 2020-07-30
categories: javascript nodejs
---

Console.log is an effective and useful tool for debugging, but have you read the documentation or dug much into it? I did and I wanted to share a few neat tricks for you to make your debugging more effective. 

We've all seen `console.log('hello world');` or something similar in our code. But what about when we want to print variables? We could use string  templates or string interpolation, such as below, or we could use something easier; format strings

```javascript
// string interpolation
console.log('this is my userName: ' + userName + '\n this is the request body: ' + JSON.stringify(req.body));

// string template version 
console.log(`this is my userName: ${userName} \n this is the request body: ${JSON.stringify(req.body)}`);
```

These are fine and they work, but console log allows us to use a format string. If you're not a C++ or Java programmer, nodejs brings in a [format util](https://nodejs.org/api/util.html#util_util_format_format_args) which gives us the ability to format strings which can make things less verbose and more type safe. 

```javascript 
// Format string
console.log('This is my username: %s \n this is the request body: %o', userName, req.body);  
```

The nice thing about a format string is it tells you what type you're expecting the username to be; operators like %o will automatically generate a string version of the object for you. Which is convenient. 

Here's a list of some of the options for a format string, source is the [NodeJS docs](https://nodejs.org/api/util.html#util_util_format_format_args).

| Option 	| Description                                                                       	|
|--------	|-----------------------------------------------------------------------------------	|
| %s     	| Will render a string on all values except BigInt, Object and -0.                  	|
| %d     	| Number, which will represent all things expect BigInt                             	|
| %i     	| parseInt(value, 10) is used for all values except BigInt and Symbol               	|
| %f     	| parseFloat(value) is used for all values                                          	|
| %j     	| JSON.                                                                             	|
| %o     	| Renders an object as a string with options of showHidden and showProxy to be true 	|
| %O     	| Renders an object as a string without the above options                           	|
| %c     	| Ignores CSS passed in                                                             	|
| %%     	| Returns a single percent sign; basically escaping an percent                      	|

# Examples

## Render a table

This could be useful if you're building a CLI tool and want to display all the options. Or perhaps render a JSON array as a table?

```javascript
// render a table:
console.table([{ a: 1, b: 'Y' }, { a: 'Z', b: 2 }]);
// ┌─────────┬─────┬─────┐
// │ (index) │  a  │  b  │
// ├─────────┼─────┼─────┤
// │    0    │  1  │ 'Y' │
// │    1    │ 'Z' │  2  │
// └─────────┴─────┴─────┘

console.table([{ a: 1, b: 'Y' }, { a: 'Z', b: 2 }], ['a']);
// ┌─────────┬─────┐
// │ (index) │  a  │
// ├─────────┼─────┤
// │    0    │  1  │
// │    1    │ 'Z' │
// └─────────┴─────┘
```

## Useful: Count how many seconds a function took to execute
I could see this one being really useful, to count how long a method or loop took to complete. 

``javascript
let myMethodCall = async (data = {}) => {
  let reply = await api.call(url, data);

  // see how long time has elapsed; can even check the current value!
  console.timeLog('methodCallTimer', reply); 

  let replyModified = await api.call(url2, reply);
  return replyModified;
}


// start timer
console.time('methodCallTimer');
let xyz = await myMethodCall();
console.endTime('methodCallTimer');

// prints methodCallTimer: 365.227ms {option: "all"}
// prints methodCallTimer: 3000.23ms
``` 

## Print the current stack trace

Lets say you have a callback you have to supply to a method, but you have no idea where that callback will finally be called; one way to solve this would be to print the current stack trace

```javascript
myGreatAPICall((data)=>{console.trace('Show me')});
// Prints: (stack trace will vary based on where trace is called)
//  Trace: Show me
//    at repl:2:9
//    at REPLServer.defaultEval (repl.js:248:27)
//    at bound (domain.js:287:14)
//    at REPLServer.runBound [as eval] (domain.js:300:12)
//    at REPLServer.<anonymous> (repl.js:412:12)
//    at emitOne (events.js:82:20)
//    at REPLServer.emit (events.js:169:7)
//    at REPLServer.Interface._onLine (readline.js:210:10)
//    at REPLServer.Interface._line (readline.js:549:8)
//    at REPLServer.Interface._ttyWrite (readline.js:826:14)
```

# Override console to write to a log file

Perhaps you want to log to a log file or provide color options. Here's how you log to custom files by overriding the existing console: 

```javascript 
const output = fs.createWriteStream('./stdout.log');
const errorOutput = fs.createWriteStream('./stderr.log');

global.console = new Console({ stdout: output, stderr: errorOutput });
```

# Asserting values

A simple assertion test that verifies whether value is truthy. If it is not, Assertion failed is logged. If provided, the error message is formatted using util.format() by passing along all message arguments. The output is used as the error message.

```javascript
console.assert(true, 'does nothing');
// OK
console.assert(false, 'Whoops %s work', 'didn\'t');
// Assertion failed: Whoops didn't work
```

There are a few more options in the docs, such as clear or group; but these to me are the most useful, thus why I shared. Why did I share? Well, most people don't both reading the documentation. I don't know how many times a coworker asked me a basic question about something that was explained in the docs; I know because I ask them if they read the documentation and 9 out of 10 times the answer is "I bang on it until it works". UGH. What can you do? ¯\_(ツ)_/¯