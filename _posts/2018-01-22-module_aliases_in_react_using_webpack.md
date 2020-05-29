---
layout: post
title:  "Module aliases in React using Webpack"
date:   2018-01-22
categories: react javascript es6 Redux create-react-app webpack
---

For my big rewrite project I'm working on, I decided it was time to start referencing modules by an alias instead of a relative or absolute path. It has a bunch of different modules, from the Redux store to an API service that almost every component or action consumed in some way. Figuring out the file path to the store or other common services was a chore.

The goal was an ES6 statement as follows:

```javascript
import store from 'app-store';
import APIService from 'api-service';
```

This is how we got there.

# Dependencies

We are using an ejected version of the create react app. This is running the latest version of React and Webpack. We're also using jest for testing and eslint for linting.

# Configure your webpack environments

The first step to adding a module is to figure out the absolute path of the module you want, then configure webpack.config.prod.js and webpack.config.dev.js. You may also need to add to other .environments.

Under the module.exports, there is a parent key - "resolve" - that contains a child object called "alias." In our version of the react app, it came bundled with the following:

```javascript
'react-native': 'react-native-web',
```

Add a key value pair for the module you want to reference; in our case, it was the store.

```javascript
'app-store': path.resolve(__dirname, '../src/store'),
```

# Package.json

In your package json file, you will need to map the module you need so the jest scripts can find things.

Add a key under the parent "jest" called "moduleNameMapper" if it doesn't exist, like you did above. This is ours:

```javascript
"app-store": "<rootDir>/src/store.js",
```

# Eslint config

In your eslintrc.json file. under the parent "rules," there probably is a child: "import/no-unresolved."  If not, add one as an array collection. Then, add the rule to ignore erroring on unresolved "app-store" which ESlint cannot statically find.

This is what ours looks like:

```javascript
"import/no-unresolved": [
  "error",
  {
    "ignore": ["app-store"],
  }
],
```

Once you have all of that, the module should run with tests passing. Then, you can run the command ```yarn start``` This should not raise any issues with the linter running or starting the server.

There you have it - a way to reuse common objects in React!



