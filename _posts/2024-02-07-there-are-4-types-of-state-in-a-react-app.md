---
layout: post
title: "there are 4 types of state in a react app"
date: 2024-02-07
categories: javascript typescript react
---

In any React application it's important to understand the type of state going on and what the different use cases are for each, today let's explore it together.

# The user session state

This is the first major state. It's a user session state. It could be stored in a cookie with a TTL, it could be stored in a browser session which clears when the tab / window is cleared or it could be stored in local storage (Not great, because that never automatically clears). Typically a user state session is either a JWT or a OAuth bearer token. This is global state that exists outside a standard React application, it persists in browser memory accessible by standard browser methods (not tied to React Lifecycle methods).

# The global state

The second major state is the global application state. This is typically in memory or in local storage, depending on the persisting requirements of the application. This is stuff that exists across dozens or hundereds of components. A few use cases come to mind:

- Multi tennant applications -- Storing theming or branding info
- Shopping cart, product catalog type of applications
- Complex workflows

This type of state can be managed by Redux (Flux pattern), manually using your own custom logic or using a library like RecoilJS. The important part here is to have a consistent way to set and modify the data, which is where Redux can be very helpful.

# The context state

An advantage of React and Hooks is that you can use the context hook. Basically, it's an interface that you can define at any level a provider then a consumer. Inside the root application for example you could set a context state to hold all state instead of using Redux. But I think it's a better tool for a small workflow or a route level context. I'll give you a few examples:

1. A page level context. For example a user admin list. You click "edit" on a user then a modal displays. The modal is independant of the list, it gets the user info from context. It allows you to seperate concerns, and inject the specific required attributes at anytime in the workflow. You can set it on step 1 and use it on step 10.

2. A workflow context. For example you need to build a wizard to compute someone's health insurance premium. Each step you gather bits and pieces of their medical information and history. The last step data could influence the next step, a great way to handle that would be to use context, store that data then in the next workflow component, allow that component to decide what to do with that state.

When it's not great is when the user has to reley on a lot of data or there are many components in the mix across various parts of the application. Eg, you load data on the home page, then modify it in the profile then modify it even further in the cart. That's better use case for Global state.

# Component state

Within react, this is the final major state. Controlled forms, `useState` hooks and things like that are the main things contained within the component state. For example, load a user list using a `useEffect` then storing it in a `userList` state hook is a great example.

# Bonus: HOC

Higher order components are useful, rather then using a context, to drill a small set of props down to dumb, pure functional components with no side effects. Eg, you need to implement a dumb list, it takes a bunch of data, triggers an action on submit but it needs to be somewhat dumb, an HOC is a good pattern to use. The HOC manages the state and composition of the components while the children handle the specific rendering.

There we have it, 4 (5 really), different and most common types of state within a React application. These are patterns I commonly use and often think about.
