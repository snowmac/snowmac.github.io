---
layout: post
title: "A quick look at data tables and Material UI"
date: 2023-03-15
categories: javascript mui datatables
---

A couple weeks ago I set-out to build a prototype for some friends of their web application ideas. They already had a design built partially in Material UI. In the past I've found most CSS frameworks and libraries to be a colossal pain, but after poking around I decided that MUI is a pretty awesome tool that I get to work with. It has led me to believe that if you're building a component library for your own needs, you're wasting time and the companies time (unless you want to do it for fun). 

# Data Tables in MUI 

The examples in the <a href="https://mui.com/x/react-data-grid/getting-started/#quickstart" target="_blank">docs</a> are somewhat clear, but not entirely. 

I had a demo recently to my friend but I could not for the life of me get the data to render properly. Here's an example of my table code. 

```javascript 
import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { CircularProgress } from '@mui/material';

export default function ProjectsList(props) {
    const columns = [
        { field: 'name', headerName: 'Name', width: 130 },
        { field: 'duedate', headerName: 'Due Date', width: 130 },
        { field: 'description', headerName: 'Description', width: 130 }
    ];

    const projects = [
        {name: 'Adams new project', duedate: 'March 31, 2023', description: 'Gotta build the prototype'},
        {name: 'Adams new project 2', duedate: 'March 31, 2023', description: 'Gotta build the prototype'},
        {name: 'Adams new project 3', duedate: 'March 31, 2023', description: 'Gotta build the prototype'},
        {name: 'Adams new project 4', duedate: 'March 31, 2023', description: 'Gotta build the prototype'},
    ]

    if(isLoading) {
        return (<CircularProgress />);
    } else {
        return (
            <DataGrid rows={projects} columns={columns} pageSize={5} />
        )
    }
}
```

You would expect a table with 4 rows and 3 columns to render. I got the columns but no row data. I saw that the pagination said 4 items on the page on page 1 of 1, but there were no grids. 

The tricky part is the documentation isn't that great. It missed one key element: talking about the row height requirement. An easy fix: 

Change this: 
```javascript
    <DataGrid rows={projects} columns={columns} pageSize={5} />
```

To this: 
```javascript
    <DataGrid rows={projects} columns={columns} pageSize={5} autoHeight={true} />
```

There you have it! A table that renders. 