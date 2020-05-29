---
layout: post
title: "Parsing JSON files made easy"
date: 2018-04-12
categories: json jsonpath regex
---

In JavaScript land I've discovered a neat tool to help you parse JSON easier and faster. I'm going to give you a sample of a JSON, I need you to parse the JSON and give me a array of all students names.

```json
  { "body": [
    {
      "name": "Adam Bourg",
      "gpa": "3.8",
      "year": "senior"
    },
    {
      "name": "Johnny Doe",
      "gpa": "2.8",
      "year": "senior"
    },
    {
      "name": "Suzy Doe",
      "gpa": "3.0",
      "year": "junior"
    }
  ]}
```

Great, small data set. I have a few options:

1. I can loop through the data set and collect the name key to store it in an array to return.
2. I can use a Filter or a map command to streamline option 1.
3. I have 3 data points, so I can just grab all 3:
  return [body[0].name, body[1].name, body[2].name]
4. I can write a regex to parse out the name.... I hate regexes they're hard to read.

# Let's evaluate the options

1 and 2 are the same and fine, but it takes a lot of effort to loop through the data set. You have to ensure the field is not empty and that the value is not undefined. This takes logical steps and code to do this.

```javascript
  function nameFinder(data) {
    let returnArray = [];
    for(let i = 0; i < data.length; i++) {
      if (data[i] && data[i].name) {
        returnArray.push(data[i].name);
      }
    }

    return returnArray;
  }
```

There you have 9 lines of code to do this one simple task. Sure you could do it as 2 or 3 using a map, but you still have to write a enumerator object and manually get the values.

Option 3 is silly. What if the value sets change? Nope can't handle more or less than 3. So we're discounting those.

Option 4 is not ideal. Most developers don't know how to write regexes and I do not enjoy doing so. They are a pain in my butt.

# The options suck: enter, JSON Path

JSON path is a lot like xPath. You give it a string and it parses and returns the set for you.

Ok, we want all our names of the students? Easy enough with JSON path:

```javascript
  $.[*].name
```

Lets [validate it](http://jsonpath.com/). Go ahead, I'll wait. Waiting..... waiting..... Ok, what did you get? I got this:

```javascript
[
  "Adam Bourg",
  "Johnny Doe",
  "Suzy Doe"
]
```

Pretty nifty huh?

# How does it work?

Ok this is the fun part. The ```$``` part refers to the document. It's like the jQuery selector. You're telling the parser you want the whole JSON tree.

The ```.``` refers to, you want the child element(s). While the ```[]``` is the subscript operator, basically you want the items within the or you supply it with a key name ex 'foo'.

Finally the ```.name``` says you want all keys by the key of 'name'. I'll admit, it's all a little weird and different. But given that and the list of operators below, you can do a lot with it.

| Path | Description                                                                  |
|------|------------------------------------------------------------------------------|
| $    | The root object/element                                                      |
| @    | The current object/element                                                   |
| .    | Child member operator                                                        |
| ..   | Recursive descendant operator                                                |
| *    | Wildcard matching all objects/elements regardless their names                |
| []   | Subscript operator                                                           |
| [,]  | Union operator for alternate names or array indices as a set[start:end:step] |
| ?()  | Applies a filter (script) expression via static evaluation                   |
| ()   | Script expression via static evaluation                                      |


# Resources

To use it in NodeJS there is a NPM package available: [JSONPath](https://github.com/dchester/jsonpath). To read more about this and see better examples please see the [original document on JSON path](http://goessner.net/articles/JsonPath/).


