---
layout: post
title: "The case for not using redux with react"
date: 2020-06-01
categories: react redux javascript 
---

Today I want to talk about Redux. For those not informed, Redux is a [Flux](https://facebook.github.io/flux/docs/in-depth-overview/) implementation of a state management system for React. Redux is an interesting and useful tool that can improperly used. 

# Why Redux

The why is really easy, components at some level have to manage state. Components have to interact with other components. Local state of components can and should be handled by that component. Class based components could use this.state mechanism or a local variable. While functional components should use the state hook for local state. 

The use case for Redux is where you share state between components, and that state is subject to frequent and regular change. A great example of this would be work for a TV company (Like I did). You have several components: Package, Offer, User, Channels, Extras etc.. which are all driven by a complex set of rules: user location, language, cost, current subscription; which all drives the offer on the screen and the packages available within that offer. 

In that example, you need a clear and concise way to manage state. When you select "X" offer; then it shows you what Channels are included, what the cost is, options for Extra's, but then say you want to see what offer "Y" provides you with; the entire section of the UI has to re-render showing you new packages, channels, and extras; some similar some not. 

Use cases like a store with a shopping cart, TV offer system, health insurance or taxes are prime examples for why Redux is useful. Which is when you need shared state that is subject to regular state changes; all between differing and discrete components. 

State management can be a bear, but Redux makes shared state management better. 

# There's more then one type of state

There is more then one type of state to care about. Here's what I think MOST applications have to worry about: 

* User auth state 
* Shared business state
* Global application state 
* Localization state 
* Local state 

Lets break them down below

## User auth state

A user logs into the system. The end result is you will get a JWT or some kind of token you need to keep track of for making API calls. This is a good thing to consider storing in Redux; plus other info, such as: Name, Email, Photo etc... 

The thing is, within the User Auth scenario, you're not going to mutate that data much. The user MAY change their name or password once in a while, but not often. The browser has better tools for storing this information, such as a cookie or local storage. The advantage here is that when the browser refreshes, the state persists, which by default does not occur with Redux. Technically yes, you can store all of your redux state in local storage, but it defaults to in memory storage; thus would be lost, on default, when refreshed. 

## Shared business state 

Recently I had to modify all the forms within the site to auto save before auto log out. We had a dozen forms across several components. Basically when your session times out, we save your survey then log out. 

I first tried using context and a local component state, but that proved to be unwieldy, not to mention the team is more comfortable with Redux. Next I decided that on a [debounce](https://chrisboakes.com/how-a-javascript-debounce-function-works/) of user input change, to automatically call Redux, save the state. That way, once 20 minutes has run out; the user's state would be in Redux then we simply save, clear site data & redirect to the login page. 

This was a better approach then context, local state or storing things on top or window because it is already understood by the team and its simple in implementation. 

This works great because the survey does not need to know about the logout page, it saves to redux. Likewise the Logout page doesn't need to know ANYTHING about the surveys, it just needs to take values from Redux and store them in the API. 

## Global application state 

Think about configuration data. What APIs to call, colors of the site, logos, branding, etc... Redux can be used to solve this problem, but this data is unlikely to change frequently unless you have use cases as to why; eg you switch to a different organization and need to show that org's branding. I would say in __most__ cases, using context within React would be a better approach then using Redux because the data does NOT change very much. You don't really need to "manage" the state. 

## Localization state

Like Global Application State, I doubt this will change much. Once a user selects "Spanish" it's unlikely to change. I would put the User's preference into Redux while reserving the the actual values to be provided from Context. There are a few reasons for this: 

1. There will be hundreds if not thousands of variables to set, I wouldn't want that stored in Redux; talk about clutter. 
2. The "Preference" could change but the actual values to that will not, 
3. It would be easy to implement a single function that takes the User's preference, goes to the API or a file, gets that selected language then loads all the keys into Context. 
4. If you didn't use context, every single component would have to be connected to Redux or have to use a HOC; either approach would be messier then relying on context; which you can get through the useContext hook for functional components. 

## Local State

Here's where I think the useState or this.setState can be really helpful. The use cases here are where you want to take user input, save it to the API and that's about it. For example, most use cases within an application would probably fall into this category. 

A wizard workflow could fall into this category. You select that client "A" belongs to category "B" and has attributes "D" and "E"; call the API and the API then returns a set of new questions to answer. Some wizards would probably be better solved with Redux; such as A + B determines C without API data, others where you only care about the state from the API would be a good use case for local state. 

A few other examples would be: 

* A contact form 
* A UI where you can "like" a post, image or something like that 
* Payment form
* Signup form 
* A user's profile or avatar
* A product for a online store 

# Final Thoughts

In my opinion mixed state management is the best approach, use case based: 
* For branding, API urls, Application specific data etc... use context and load it at application start. 
* For user auth, use cookies or local storage. 
* For Localization, store the preference in Redux or local storage, providing values through context. 
* For global data that has to be shared between components (Surveys and logout component), use Redux 
* For most other things, use local state

Soon, I'll be following up with an alternative to Redux: An Introduction to React Hooks. 