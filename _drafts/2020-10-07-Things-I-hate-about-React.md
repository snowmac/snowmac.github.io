---
layout: post
title: "Things I hate about React"
date: 2020-10-07
categories: react javascript
---

I'm not a hater, but there are some things in the modern javascript community that drive me bananas. These are stupid, small, minor things but I keep scratching my head as to why do they do it this way? So I wrote a ranty post about it. I do build a LOT of things in React, but some things are silly. 

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

# Styled components

I'll write them, I'll use them but they're really stupid. 

