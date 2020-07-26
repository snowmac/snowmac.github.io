---
layout: post
title: "Lets stop being stupid about security"
date: 2020-07-26
categories: 
---

I hate it when I run across what is reported to be an epic hack involving Russians, Chinese or spies only it turns out the hacking victims were not taking any form of basic security seriously. Its like asking Bonnie and Clyde to rob a bank where the combo is printed on a large banner outside the vault and there are no keys to any safe deposit boxes. Or it's like letting the fox get inside the hen house. 

Unfortunately the victims in this case seem to be the US Government. The article is titled: ["How the Russians penetrated Illinois election computers - ABC7 Chicago"](https://abc7chicago.com/russia-russian-hacking-elections-illinois/3778816/).

What was the hack? SQL injection. SQL INJECTION!!@!@!! What the #$%@? Are we living in the 90s? What the heck are developers doing? Sadly, I've encountered the problem on projects I've worked on within the last YEAR. WTF is wrong with people? Are we lazy or stupid or a bit of both? 

# Let me educate you on SQL Injection 

Here's an innocent query; let's say we're using Postgres and NodeJS

```sql 
SELECT firstName, lastName, email From users where email = "adam@adambourg.com"
```

Not bad, but lets see how we can build it in Javascript: 
```javascript
async function lookupUserByEmail(emailAddress) {
    if(!emailAddress) {
        throw "Email address is required!";
    }

  return await db.any(`SELECT firstName, lastName, email From users where email = "${emailAddress}"`)
}
```

There is a simple method to ensuring we have an email and fetching a user record from the database. The trouble is, we're doing string interpolation, meaning we take that query and inject ANYTHING from the emailAddress variable. No big deal, right? 

What if email address is this: 

```sql
1 OR 1=1; 
```

That means it would match on the first value, 1, which probably won't match anything or on 1=1 which is literally interpreted by SQL as does 1 equal 1? Which is always true. Thus would return EVERY record in the system. 

# How could someone use SQL Injection to do harm?

Assume the hacker has no knowledge of the system and does this: 

```sql 
1 or 1=1;
```

Now I've got a list of all the records in the table; great, what if I want to know what options are present in the system? Well, do this: 

```sql
1'; SELECT c.relname FROM pg_catalog.pg_class c LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE c.relkind IN (‘r’,”) AND n.nspname NOT IN (‘pg_catalog’, ‘pg_toast’) AND pg_catalog.pg_table_is_visible(c.oid); 
```

Version?

```sql
1'; SELECT version();
```

Postgres users?

```sql
1'; SELECT usename FROM pg_user;
```

Users and password hashes? No problem: 

```sql
1'; SELECT usename, passwd FROM pg_shadow — priv;
```

Here's the thing if you don't sanitize your inputs, you are venerable to so many easy hacks. In fact there are [many](http://pentestmonkey.net/cheat-sheet/sql-injection/postgres-sql-injection-cheat-sheet), [dozens](http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet) of [different](https://portswigger.net/web-security/sql-injection/examining-the-database) [guides](https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/) on [any](https://www.sqlinjection.net/table-names/) and [all](https://download.oracle.com/oll/tutorials/SQLInjection/index.htm) [versions](https://www.blackhat.com/presentations/bh-usa-05/bh-us-05-fayo.pdf) of [SQL](https://docs.microsoft.com/en-us/sql/relational-databases/security/sql-injection?view=sql-server-ver15). 

# How do I protect myself? 

Unlike the idiots in Chicago, buying an expensive Cisco Firewall will not do anything to protect you. In fact, it will only cause you to feel more secure thus take more risks. No what you need is real security. Basic security. It's like putting a lock on your door type of security. 

# Enter Parameterized Queries AKA "Prepared statements"

Just about every SQL library supports Parameterized Queries. If they don't you need to find a new lib to use. 

Example in PQ: 

Given our example from above, here's what a safe query would look like: 

```javascript
async function lookupUserByEmail(emailAddress) {
    if(!emailAddress) {
        throw "Email address is required!";
    }

  return await db.any(`SELECT firstName, lastName, email From users where email = "$emailAddress"`, {emailAddress});
}
```

Well, that was simple! Basically $ with out the brackets are treated as a normal string, you can keep the string template literal (the back ticks) or use quotes instead; then you're dumping email address into an object that gets passed to the db's any method which does all the work. 

This works:
```javascript 
lookupUserByEmail('adam@adambourg.com');
```

This does not work as the hacker expected:

```javascript 
lookupUserByEmail('1 or 1=1;');
```

# Prepared statements examples 

A few examples of the method body in other languages using this safe method: 

```php
$stmt = $dbh->prepare("SELECT firstName, lastName, email From users where email = (?)");
$stmt->bindParam(1, $email);
$stmt->execute();
```

```java
String sqlQuery = "SELECT firstName, lastName, email From users where email = (?)";
PreparedStatement prepStmt = conn.prepareStatement(sqlQuery);
prepStmt.setString(1, "adam@adambourg.com");
prepStmt.executeUpdate();
prepStmt.close();
```

# Does your ORM support prepared statements? 

Active Record does right out of the box; it's automatic, similar for Sequelize. Should you turn it off, like this [idiot says](https://medium.com/@devinburnette/be-prepared-7768d1a111e1)? Hell NO!