---
layout: post
title: "Simplifying Logic Using Maps"
date: 2020-06-18
categories: javascript nodejs code examples 
---

Today I was working on a program that scrapes data from a CSV, maps the records to a custom JSON structure then exports it as a custom file for injest into the system at a later date. The trouble was I was using a TON of IF statements. Today, I'm going to show you how to transform a massive if statement into a much simpler map.

# Preconditions

I'm using the NPM module [CSVTOJSON](https://www.npmjs.com/package/csvtojson). Here's how I'm using the code: 

```javascript 
csvProcessor().fromFile('./myRecords.csv).then((values) => {
    values.forEach(rowFormatter);
}); 
```

rowFormatter is what I'm going to be showing you the rest of the article. 

# Row Formatter 

Row Formatter is really simple, but the guts aren't. Here's a similar method to the one I was writting today. 

```javascript
function rowFormatter(row) {
  let answers = {}; 

  // looking at each field in the row of the provided CSV
  for (let [key, value] of Object.entries(row)) {
    if(key==='Account Name') {
      answers['accountName'] = value; 
    } else if(key==='Line of Business') {
      answers['lineOfBusiness'] = value; 
    } else if(key==='Industry Sector') {
      answers['sector'] = value; 
    } else if(key==='Industry Sub-Sector') {
      answers['subSector'] = value;  
    } else if(key==='Country') {
      answers['country'] = value;
    }
  }

  return {
    answers, 
    guid: uuid.v4()
  };
}
```

As you can see in this first example we're taking values such as 'Industry Sub-Sector' and mapping them to a simpler key like 'subSector' each key is different and many are not at all similar to the header names. This one function doesn't seem so bad, but I'm working with over 100 columns and 4000 rows of data; this nested if inside a for loop is MADNESS. 

# Enter Map Building

No I'm not a cartographer nor am I the master chief, today we're going to build a simplified map. For this example, I need to take an English title of a column, then transform it into a json key, stuff it into answers; manipulate it then return to the caller for dynamic SQL generation. But writing the if statements is boring and tedious. 

Here's the map I built

```javascript 
const headerNameToFieldName = {
  'Account Name': 'accountName',
  'Line of Business': 'lineOfBusiness',
  'Industry Sector': 'sector',
  'Industry Sub-Sector': 'subSector',
  'Country': 'country'
};
```

With the map from the column header to the expected database value in place, I can now map my json to the keys and complete the function. 

```javascript
for (let [key, value] of Object.entries(row)) {
  let keyName = headerNameToFieldName[key];
  if(keyName) {
    answers[keyName] = value; 
  }

  // special logic for maps that don't exist
}
```

As you can see, the loop is SO much simpler. Not to mention it's really fast; why? We're not doing a logical check on every key; we're looking up the key, ensuring the key is real, then using it to set a value on answer response object. This is an O(n) operation either way, but it's slightly faster because you're only using the map as a look up instead of a lot of logical checks. Not to mention this is more easily reasoned about then the if statements. 

# Compare the code

They're both the same number of lines; but which one is easier to read? 

## Before Refactor
```javascript
function rowFormatter(row) {
  let answers = {}; 

  // looking at each field in the row of the provided CSV
  for (let [key, value] of Object.entries(row)) {
    if(key==='Account Name') {
      answers['accountName'] = value; 
    } else if(key==='Line of Business') {
      answers['lineOfBusiness'] = value; 
    } else if(key==='Industry Sector') {
      answers['sector'] = value; 
    } else if(key==='Industry Sub-Sector') {
      answers['subSector'] = value;  
    } else if(key==='Country') {
      answers['country'] = value;
    }
  }

  return {
    answers, 
    guid: uuid.v4()
  };
}
```

## After Refactor

```javascript
function rowFormatter(row) {
  let answers = {};

  const headerNameToFieldName = {
    'Account Name': 'accountName',
    'Line of Business': 'lineOfBusiness',
    'Industry Sector': 'sector',
    'Industry Sub-Sector': 'subSector',
    'Country': 'country'
  }; 

  for (let [key, value] of Object.entries(row)) {
    let keyName = headerNameToFieldName[key];
    if(keyName) {
      answers[keyName] = value; 
    }
  }

  return {
    answers, 
    guid: uuid.v4()
  };
}
```