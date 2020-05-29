---
layout: post
title: "Deploying a Node.JS application to Azure"
date: 2018-04-02
categories: nodejs expressjs azure windows paas
---

My new job has taken me to interesting new adventures. This job has introduced me to the fun of trying to get Node.JS and other open source tools to work with the latest versions of Windows.

# The pain of Node Gyp

There's a module, "node-gyp", it's a node module for using Python to conduct various tasks that are easier to do in python. You probably don't directly use it, rather a dependency of a dependency of a dependency you must have for your application critically relies on it. Well, my friend you just got long day ahead of you while trying to deploy this to an Azure PaaS.

There are few options:

1. Check your node_modules into the repo and push them up on deploy. This only works on Windows development machines not a Mac or Linux machine.
2. Push the code as normal, but deploy through a CI/CD server.
3. Copy the node_modules up to the PaaS and hope nothing ever changes.

To solve this problem we started by just copying up the node modules, then tested. This resolved the issue of the node gyp not installing, however; the upload took about 20 hours.

You can read more about this approach in the article: [Installing native nodejs modules on Azure App Services during Git Deployment](https://ourwayoflyf.com/installing-native-nodejs-moduleson-azure-app-services-during-git-deployment/). That helped us out a lot to get over the node gyp hurtle.

# The joy of Express JS

In a typical Express JS project there is a folder called 'bin' in the project root directory. Inside this folder is a file called 'www'. This is not so nice, because the execution environment of Azure runs the www file in the bin folder from the bin folder. Whereas when you run locally on the command line, you're typically running either `node app.js` or `npm start` from the project root.

That is a big change because it changes the current path of the project which means that it will look for things that the 'app.js' file is calling within the bin directory not the project or 'wwwroot' directory.

To get around this issue you have to update the package.json so the 'start' script points to either 'node ./app.js' or 'node ./www'. We opted to have it target app.js since we already where doing a lot of other things within that.

These were the two issues we resolved:

1. We resolved the fatal error that we couldn't find views:
  > Failed to lookup view \"index\" in views directory \"D:\\home\\site\\wwwroot\\bin\\views\"
2. We also had a similar issue where it was looking for the .env file from the dotenv node module in the bin directory. By moving the www down then updating config we were able to save this headache

If you decide to move the www file into the project root, please change the in side the www file from:

```javascript
require('../app.js')
```

To:

```javascript
require('./app.js')
```

This will refer to the app.js in the current directory instead of the parent which is where the app is now that you're calling it from the project root.

# Update your Web.conf file

This is the magic of the Azure service. This is the config the Azure uses to load the application into the PaaS.

Change this:
```xml
<add name="iisnode" path="bin/www" verb="*" modules="iisnode"/>
```

To this:
```xml
<add name="iisnode" path="www" verb="*" modules="iisnode"/>
```

Change this:
```xml
<action type="Rewrite" url="bin/www"/>
```

To this:
```xml
<action type="Rewrite" url="www"/>
```
Once you move the files, update the web.conf file and update the www paths you should commit and push these changes. Once that's done you should have both local and remote application start working correctly.

# Conclusion

This short blog post is the summary of many days of debugging and exploring a bunch of different ideas. While I'm not familiar with Azure running Windows there are a few common points that could speed things up next time:

1. Ensure that the Windows path has all the right contexts
2. Do not use Native Addons within Azure PaaS (sounds like it will never be supported)
3. Restart the server often
4. Assume at first the problem is a config / environment issue that can be easily fixed, do not panic thinking it's the code base, especially if migrating from Linux
