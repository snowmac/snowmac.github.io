---
layout: post
title: "ClassNames drives me crazy"
date: 2020-10-07
categories: react javascript
---

I'm not a hater, but there are some things in the modern javascript community that drive me bananas. These are stupid, small, minor things but I keep scratching my head as to why do they do it this way? So I wrote a ranty post about ClassNames in React. It's enlighting and silly.

# Classes in react 

Because we're fancy pants React developers we have to write new and exciting ways to do the same old same old, enter the `className` property. Because we're **always** writing dynamic code, we have to write a bunch of code for a single className. The class name attribute only takes 1 argument: a string or a variable. It cannot be a list. 

Enter Example 1 from the [React's documentation](https://reactjs.org/docs/faq-styling.html): 

```javascript
// pass as a string
render() {
  return <span className="menu navigation-menu">Menu</span>
}

// pass as a variable built by javascript
render() {
  let className = 'menu';
  if (this.props.isActive) {
    className += ' menu-active';
  }
  return <span className={className}>Menu</span>
}
```

What does className actually do? It appears NOTHING at all. Why can't we use `class`? Because we're React Developers! It pretty much comes down to the fact that `class` is a reserved word in [Javascript and by extension JSX](https://stackoverflow.com/questions/46989454/class-vs-classname-in-react-16/46991278#:~:text=class%20is%20a%20keyword%20in,has%20changed%20in%20that%20regard.&text=Token%20class%20denotes%20that%20the,follows%20is%20a%20class%20declaration.) But the documentation does not give this as a reason why!

# Why is this a problem? 

Well, you can in fact pass in strings, but if you need to use a variable, thats all it does, it takes a string. So to get dynamic behavior you have to write it. Duh, Adam, CSS you'd have to write it anyways. Well, yeah, but if we're extending existing markup and code, can't we make it better? 

Enter [CLSX](https://www.npmjs.com/package/clsx), [classnames](https://www.npmjs.com/package/classnames#usage-with-reactjs) or the [DIY approach](https://programmingwithmosh.com/react/multiple-css-classes-react/): these are great, but if we're going to use classNames={} can't it automatically support dynamic nature? I'd love to see this (without an extra lib, or method call!): 

```javascript
<div className={['myStrongClassName', myVariableOfClasses, myMethodCall(), isActive?activeStyle:inactiveStyle]}>
```

No wrapping it in method calls, just one approach. Ugh. 

End rant 