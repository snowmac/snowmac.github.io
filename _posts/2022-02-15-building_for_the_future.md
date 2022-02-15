---
layout: post
title: "Building for the future"
date: 2022-02-15
categories: designing software
--- 

In my early days of professional programming, I had an internship at my university’s rec center. I was a web developer and I was tasked with building an employee certification tracking system. New to the idea of reusability and building for the future I was pretty nervous and did not understand what the implications where to implementing 15 column table, 3 columns for each certification. The certification then mapped into the UI and each field was manually generated. I stored the date certified, date expires and some other meta data in the 3rd column. 

Come 6 months later, the certification people said that these 3 certs are going away and these 2 are being added. Refactoring was a massive problem. It was difficult to make the change. After that I learned my lesson, next time, build a generic solution where you can add or remove N number of elements and items. If the client needs a new “category” of the same type, no problem, here’s a handy interface for them to do it. 

What I should have done would be a database structure like this: 

```javascript
Table name: CertificationTypes
Column name: id, type: Primary Key
Column Name: name, type: varchar(255)
Column Name: startDate, type: varchar(255) 
Column Name: endDate, type: varchar(255) 
Column Name: isActive, type: boolean, default: true 

Table name: StaffCertifications
Column name: id, type: Primary Key
Column Name: dateStarted, type: varchar(255) 
Column Name: dateExpired, type: varchar(255) 
Column Name: comments, type: text
Column Name: certificationTypeID, type: Foreign key 
Column Name: staffID, type: Foreign key

Table name: StaffMember
Column name: id, type: Primary Key
Column name: name, type: text
Column name: email, type: text
Column name: phoneNumber, type: text
```

Then it would have been a SQL join: 

```sql 
SELECT ct.id, ct.name as certName, ct.isActive, sc.certificationTypeID, sc.dateStarted, sc.dateExpired, sc.comments, sc.staffID FROM CertificationTypes as ct 
INNER JOIN StaffCertifications as sc
ON sc.certificationTypeID = ct.id
WHERE ct.isActive = true AND sc.staffID = ${staff_id_input}
```

Then just loop through each record and display a result for that specific employee’s medical certifications. That was 12 years ago, something hard to fathom then was a quick blurb on my text editor. It’s easy now to think like this. To think about how my software could be used and build in flexibility. 

Another example of this is at my current job. One coworker isn’t able to work on an ETL Process so they assigned it to me instead. Our boss wanted it done as a synchronous process, I recommended async. Here’s why, we’re building a multi tenant application to be delivered as mostly a SAAS model with consulting services on the side. The trouble with the single endpoint sync process is that it will handle the current client use case of 1000-2000 records imported just fine. But what happens when we scale it up and out, we have 100,000 records or even 1,000,000 from a future client? What do we do then? Refactor? 

## How about we build it right from the beginning? 

Enter scale and the ETL Process. We have to process the file, validate it and return an error if it’s not valid (any row) or insert it into the database. There are several distinct tasks: 

* Queue up the request 
* Validate the data
* Message Redis the current status
* Insert into DB 
* Message Redis the current status
* Delete the request from the queue

What’s nice about using a worker pattern and a tool like Node-Resque is that while the stuff is processing in the background in a separate service, we’re not locking up the process of the main thread of the backend API. If we didn’t do that and a client passed us a 1,000,000 record file; then we still would not be blocked I the async approach vs the sync approach. 

In the future when building software, it’s important to think about how this feature will be used and consider if it’s valuable to make it so that you can more easily handle more load, new requirements (eg categories) or even new data points. 
