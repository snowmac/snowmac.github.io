---
layout: post
title:  "Redux Demystified"
date:   2018-01-11
categories: react javascript es6 Redux
---

Today we're going to look at Redux. Redux is a popular tool to use with React. We're going to explore the topic and talk about why you should consider using it.

# What is Redux?

Redux is all about state (data) management. It takes the place of doing a traditional MVC approach where data is stored in instances of models and replaces that data storage with a global storage location. Typically stored on Window or top. The data can be stored in local storage or in a cookie.

# Why Redux?

MVC is great, but for storing data it can be very difficult to reason about the freshness of data, how data mutates, or who has access to that data. Redux simplifies all of the complexity around state management by having 1 standard way of interacting with the state: A reducer.

# Model of Redux

Redux at its core is a pub/sub model. Purely event driven. A component gets its state from the Redux Store. The component takes an action, like clicking a button which triggers an action to fetch data. The action gets data from the API, then notifies the system it's done. Once that occurs, Redux check's it's list of reducers to see if there is something built to handle that action response. If there is a reducer to handle that response: it handles it then possibly modifies state.

The state change (if there is one) triggers Redux to update all relevant connected components, which will force a redraw in most cases, thus refreshing the screen.

![Fancy picture of the Redux model](/assets/img/jan2017_redux_pattern.png)

# What's a reducer?

When a reducer is invoked, through dispatch, it receives a message stating what event is occurring, what the new proposed state could be and the current application state.

The reducer is a standard API for mutating the state of the Redux store. The code is pretty simple, it looks at the incoming action type, the proposed data and the current data then makes a decision about what to store.

```javascript
  function myReducer(state = initalState, action) {
    switch (action.type) {
      case 'SET_NOTIFICATION':
        return { text: action.text, type: action.kind };
      default:
        return state;
    };
  }
```

You can see in this example when the event we're getting passed in is to set a notification, we take the current information; text and type and pass that to be stored into Redux. Otherwise, we default to returning what is already there.

Testing this is so super easy. It's a pure function.

```javascript
  it('testing the set notification case', () => {
    const actionData = {
      text: 'Hello World!',
      type: 'SET_NOTIFICATION',
      kind: 'success'
    };
    const reducerValue = myReducer({}, actionData);
    expect(reducerValue.text).toEqual(actionData.text);
    expect(reducerValue.type).toEqual(actionData.kind);
  });
```

# What's an action?

An action is invoked by a component /module/class. Basically, it handles the interaction between the API and reducer. There are two basic types of actions:

1. An action that notifies of an event. Eg, I need to set an error message or force a sign out.
2. An action that calls an API then passes the reply to the reducer to update state.

Actions can be pure functions, but they could also call out to an API service.
```javascript
  const ErrorMessage = (message) => {
    return (dispatch) => {
      dispatch({type: 'ERROR_MESSAGE_REQUEST'});

      axois.post('http://localhost:3000/errors', message).then((response) => {
        dispatch({type: 'SET_NOTIFICATION', kind: 'error', message: response})
      });
    };
  };
```

There are many styles of writing actions, but I always write mine in the style of being called in Context thus having Dispatch provided. There are other ways of doing it but this wraps the action and trigger together, which I like a lot. Axois is a 3rd party library I use to make API calls.

# Dispatch, Store, and Connect?

## Store
Let's start with Store. The store is where all your state is stored. It has a restricted API, but you can change the "state" or "data" when you use a reducer.

## Dispatch
Dispatch is something like pub/sub; it's the messaging queue. It's the mechanism that you let Redux know something is happening. Oh, I'm getting data! Oh, I got an error! It's part of the Redux API. It's the pipeline in which things like reducers are called.

## Connect
Connect is the method of binding React components to the Store. Basically, you use something like:

```javascript
  const mapStateToProps = (state) => {
    return { type: state.notification.type, message: state.notification.message };
  };

  export default connect(mapStateToProps)(MyClassName)
```

This basically takes the state of the key 'notification' from Redux and shoves the data into the component. Possibly forcing a redraw (if it changes the props or state).

# Can I access the state without connect?

Yes, you can. You can read the state, but you cannot modify the data without a Reducer or javascript hacking. The read-only way is to directly query the store:

```javascript
  store.getState(); // returns the full store as a JSON object
```

# Wrap up

This wraps up the quick and dirty explanation of Redux as how I currently understand it. If you have any feedback, please find me on twitter, @coffeeski or send me an email prodevmentor (at) gmail.com. Thank you for reading!
