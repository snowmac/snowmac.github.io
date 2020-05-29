---
layout: post
title: "Installing Kotlin on Windows"
date: 2018-05-01
categories:
---

Installing Kotlin on Windows can be difficult, hopefully this guide will help you.

# Assumptions
* Windows 10
* Kotlin 1.2.30
* Java 10.0.1
* Gradle 4.7
* Postgres 10.3

# Shell? What shell?

If you follow the install process, I've been able to use this with the Powershell or Git Bash.

# Install proccess

1. Install the JDK from Oracle. Get the latest version.
2. Install Gradle using ```choco install gradle```.
3. Install kotlin using ```choco install kotlin```.

# Configure the environment

You're going to need to set a system environment variable called 'JAVA_HOME'. Oracle has a doc for this: https://www.java.com/en/download/help/path.xml

Basically go to:
1. Control Panel ->
2. System ->
3. Advanced System Settings ->
4. Type your password in ->
5. Advanced Tab ->
6. Environment Variables ->
7. Under "User variables"
8. New... ->
9. "variable name": "JAVA_HOME"
10. "variable value": Path to the java folder, mine is "C:\Program Files\Java\jdk-10.0.1"
11. Click ok

Now open the terminal, you should be able to run gradle build on the project now

# Fixing common errors

## ```com.sun.tools.javac.util.Context```

This error occurs when you don't have JAVA_HOME set or if you set it but haven't restarted your Windows shell.

## ```e: java.lang.ArrayIndexOutOfBoundsException: 452 :compileKotlin failed```

You will get this if the project's version of Kotlin in the build.gradle file doesn't match what's on the system.

Open the file 'build.gradle' and ensure that the key 'ext.kotlin_version' matches the version above under assumptions.

## Gradle won't start the application

Given the output below:

```shell
$ ./gradlew bootRun --stacktrace

FAILURE: Build failed with an exception.

* What went wrong:
Could not determine java version from '10.0.1'.
```

The fix is to modify the file: 'gradle/wrapper/gradle-wrapper.properties', ensure the line `distributionUrl` has the correct URL for the version of gradle you're using. For our project it was 4.7 with 'https\://services.gradle.org/distributions/gradle-4.7-bin.zip'.

Hopefully this guide will help you get your Kotlin project running on Windows. On my machine, it took me about 3 days to figure out, with little helpful step, by step, guide to get Kotlin & Spring Boot running.
