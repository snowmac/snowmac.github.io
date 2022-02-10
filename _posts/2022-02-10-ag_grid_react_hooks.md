---
layout: post
title: "AG-Grid and React Hooks"
date: 2022-02-10
categories: productive javascript programming
--- 

A coworker of mine is trying to integrate his UI code with my GraphQL Resolver code. What he wanted to do was on each button push make a call to the backend, to add a row item to a list. The trouble with this approach is that this is a CRUD type API call. It's a wizard that collects a bunch of required attributes up front than at the end calls an API to create the record with all required attributes. 

Calling the API early each time and saving state off is a bad idea for the reason of data preconditions. Not to mention it would generate a ton more API calls. He said he was going to reach-out for help because he doesn't know how to do this with React and AG-Grid. 

# First we use the use state hook 

<a href="https://reactjs.org/docs/hooks-intro.html" target="_blank">Hooks</a> are lovely. It allows us to save the state of the application into a variable / structure that then React uses to manage the lifecycle. Using array destructuring, we get to variables: categoryCodeList and setCategoryCodeList. `setCategoryCodeList` is a method that mutates the data behind the state while `categoryCodeList` is the data itself. 

```javascript
const [categoryCodeList, setCategoryCodeList] = React.useState([]); 
```

# Next we create a subcomponent

Next we create a sub component called `AddToCartButton`. We put it inside the main <MyGrid> component to be used only within the context of this grid system. Therefore we get access to the `setCategoryCodeList` method without having to do a reference or other stuff to get the state to save. It makes our lives easier. 

```javascript
const AddToCartButton = (props) => {
  return (
    <Button onClick={() => setCategoryCodeList([...categoryCodeList, props.value])}>Add to cart</Button>
  )
}; 
```

# The grid options

Next we use the <a href="https://www.ag-grid.com/javascript-data-grid/column-definitions/" target="_blank">colDefs</a> option from the <a href="https://blog.ag-grid.com/customising-react-data-grid-with-hooks-and-functions/#cellrenderer" target="_blank">Ag-Grid Documentation</a>. It allows us to set a bunch of fields, names as well as a cellRenderer which is a React Component. 

```javascript
const colDefs = [
  { field: "make" },
  { field: "price" },
  { field: "add to cart", cellRenderer: "addToCartButton" }
]
```

Finally when we render the AgGridReact Component, we pass in a call to make the cellRenderer to the correct component. 

```javascript
  <AgGridReact
      defaultColDef={{sortable: true, filter: true }}
      pagination={true}
      rowData={data}
      columnDefs={colDefs}
      frameworkComponents={{ addToCartButton: AddToCartButton }} 
  >
  </AgGridReact>
```

# Final Solution

Here's the final solution to this problem. 

```javascript
import React, { Component } from 'react';

export const myGrid = ({ data }) => {

const [categoryCodeList, setCategoryCodeList] = React.useState([]); 

const AddToCartButton = (props) => {
  return (
    <Button onClick={() => setCategoryCodeList([...categoryCodeList, props.value])}>Add to cart</Button>
  )
}; 

const colDefs = [
  { field: "make" },
  { field: "price" },
  { field: "add to cart", cellRenderer: "addToCartButton" }
]

return (
  <AgGridReact
      defaultColDef={{sortable: true, filter: true }}
      pagination={true}
      rowData={data}
      columnDefs={colDefs}
      frameworkComponents={{ addToCartButton: AddToCartButton }} 
  >
  </AgGridReact>
);

}
```
