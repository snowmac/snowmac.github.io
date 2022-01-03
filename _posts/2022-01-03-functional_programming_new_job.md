---
layout: post
title: "Functional Programming: tap"
date: 2022-01-03
categories: functional programming new job
---

Happy 2022! Life is new, it's a new year and I've started a new job... ish. More on that here. I've been at my current job for nearly 4 years all as an happy independent contractor! Well, after a tremendously hard year personally, I'm back at it. I've dropped the security assessor role and moved back into full time development role. Luke is now 2 and a half and growing like a weed. We're hunting for a new house and have put in several offers. Hoping this one is the house we get. 

All that aside, I've joined a new team doing Javascript development using TypeScript, functional programming and GraphQL with a NoSQL / Graph Database. Interesting and super complicated. The code they write makes me feel like a new programmer all over again. Growth is good but it can be hard. 

One thing I wanted to do is to document some of the really confusing examples of code. One of them is tapP. The project I'm on decided it would be a really good idea to borrow Functional Programming (FP) concepts from various libraries, wrap them into a custom package that gets included throughout the various frontend and backend applications that they write. Googling tapP yields unreliable results because it doesn't exist in the open web. 

# Let's start with Tap

In Ruby you can use `.tap` to tap into a method chain, a great example of that is to use a block with it to perform some kind of specific action. For example sending a 2 factor code on creation of a new user: 

```ruby
user = User.new(params).tap do |u|
    u.sendFactorCode
    u.sendWelcomeEmail
    # Do other helpful things on create
end
```

It allows you to chain other method calls within a method chain. It works similar in Javascript with <a href="https://ramdajs.com/docs/" target="_blank">Ramda</a>. Here's a nasty chain to debug without tap: 

```javascript 
results.comments
 .filter(forThisFile)
 .forEach(updateComment)
 .forEach(updateVariableComment)
```

In this example you want to filter before each foreach, you could do this: 

```javascript
let x = results.comments.filter(forThisFile);

console.log(x)

let y = x.forEach(updateComment);

console.log(y); 

z = y.forEach(updateVariableComment); 
```

Using tap

```javascript
results.comments
 .filter(forThisFile)
 .map(R.tap(debugPrintComment))
 .forEach(updateComment)
 .map(R.tap(debugPrintVariable))
 .forEach(updateVariableComment)
```

Code borrowed from <a href="https://www.tabnine.com/code/javascript/functions/ramda/tap" target="_blank">here</a>. 

R.tap can be useful. What it does is it takes the current data passed to it, passes it to the named function it's calling then does not return that function's result, instead it returns the data that was called with it. Eg:

`.map(R.tap(debugPrintComment))` -> .map is called on an array; it calls the method inside n times with the elements of the array. R.Tap takes each call, passes the data to the method `debugPrintComment`. It discards the return value of debugPrintComment and instead returns the element that it called debugPrintComment with. 

This is useful to debug statements but also for creating records within context. 

tapP works similar but with promises. Tap P returns a promise instead of a value. 

Here's an example of the weird code in the new project: 

```javascript 
await user.createOne({ context })(doc).then(tapP(Auditor(context, 'create')))
```

Instead of calling .map, we're using a promise structure so we can call .then on the user create call, then tap it, call another method to allow us to create an audit record. 

It's more complicated then variable assignment but it can be a bit more elegant when doing a bunch of chaining.... 

I'm not sure I like it or not, I'll reserve judgement for later. 
