---
layout: post
title: "Using Chatgpt to write SQL"
date: 2023-11-30
categories: chatgpt sql 
---

Stack Overflow sucks. The code is sometimes helpful, many times its not, many times it's plain wrong. GitHub Copilt and ChatGPT are excellent tools and are really useful for getting a really fast, specific answer that you can easily ask clarifying questions. I love using it to write complicated things. 

As you could probably tell, my post <a href="https://www.adambourg.com/ai/engineering/2023/11/24/Unlocking-the-Power-of-AI-A-Developers-Guide-to-Successful-Prompt-Engineering.html">Unlocking the power of AI</a>, was written by.... you guessed it... an AI. Yes, I have become AI obsessed. Even to the point of taking an <a href="https://www.udemy.com/course/data-science-and-machine-learning-with-python-hands-on/" target="_blank"> Udemy course on AI & ML</a>. I believe that AI is the future of computing, that is in addition to quantum computing. In order to stay current, we need to embrace the tooling, the ChatGPT, the GitHub Copilot, and other tools and find ways to integrate them into our workflows, applications and boost our productivity. ... Now off my soap box. 

Today, I'm going to show you a complicated query, I used a query coming from a looker report, but I need to scope it within X hours for a batch process. My boss had some interesting yet vauge ideas on how he would approach it, I decided to do it every x hours for the updated and created fields. I wasn't sure how to do that in Postgres but ChatGPT rescued me. 

Here's my prompt for ChatGPT:

```markdown 
Hello ChatGPT. I have a complicated SQL query I am trying to build. The query is listed below. We're joining the following tables: 

* users
* onboardings
* pro_profiles
* user_favorite_products  
* subscriptions
* orders

The query works fine. But the query we want to run is to check all of the above tables, each one has a created and updated datetime field. We want to check the fields of each of these items and include the ones that have been update the most recently. Our plan is to run this query in a batch service every 24 hours but that is going to be configurable to run at x hours. So we could reconfigure it to run every hour, or every 36 hours. Basically using an environment variable to set the hours, which I will pass into this query. 

Basically we want to pull in the record if it has been updated or created in the last x hours according to that field on each table. If orders is updated, but pro-profiles is not, we will pull the data regardless, but we want to pull the most recent data. If nothing has been updated within the last x hours, we don't want to pull the data and have it excluded in the output. 

We're Knex to do the query builder, running in the raw mode and our database is Postgres. 

The query is below: 

```sql
SELECT 
	users.id 
    -- other fields
FROM users
    -- my joins (about 6 of them)
WHERE users.role IN ('customer', 'customer pending');
\```

Can you help us with our query?
```

I included the real query, but put it in as a sanitized version here (no real code/sql) for the blog. I loved the response it gave me: 

```markdown
Certainly! It looks like you're trying to retrieve records from various tables based on the most recent update or creation time within the last X hours. To achieve this, you can modify your query to include a condition that checks whether the record has been updated or created within the specified timeframe.

Here's an example of how you can adjust the query using Knex.js with raw mode:

```javascript
const knex = require('knex')({
  client: 'pg',
  connection: {
    // your database connection details here
  },
  // other configuration options
});

const xHours = 24; // You can adjust this value based on your configuration

const query = `
SELECT 
    users.id,
    -- other selected fields
FROM users
    -- your joins
WHERE 
    users.role IN ('customer', 'customer pending')
    AND (
        users.created >= NOW() - interval '${xHours} hours'
        OR users.updated >= NOW() - interval '${xHours} hours'
        -- Add similar conditions for other tables
    );
`;

knex.raw(query)
  .then((result) => {
    console.log(result.rows);
  })
  .catch((error) => {
    console.error(error);
  })
  .finally(() => {
    knex.destroy();
  });
\```

This modification adds a WHERE clause that checks whether the record has been created or updated within the last X hours for the 'users' table. You can replicate this pattern for other tables like 'onboardings', 'pro_profiles', etc., by adding similar conditions.

Make sure to replace the placeholder comments with the appropriate fields and join conditions for other tables. Also, ensure that your database connection details are correctly configured in the Knex.js initialization.

Feel free to adapt the query to your specific needs and let me know if you have any questions or if there's anything else you'd like assistance with!
```

As you can see, ChatGPT gave me a specific and helpful idea, 

```sql
SELECT * FROM users
WHERE users.role IN ('customer', 'customer pending') AND (
users.created >= NOW() - interval '72 hours'
OR users.updated >= NOW() - interval '72 hours'
)
```

That's really helpful and specific advice. I tested it with the 72 hour interval and that really helped me find records updated in the last 72 hours. I'm not that familar with timestamps and intervals in Postgres so ChatGPT really helped me with some real, functional code. 
