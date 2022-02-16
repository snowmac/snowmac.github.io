---
layout: post
title: "Wordle Exposed"
date: 2022-02-16
categories: wordle hacks
--- 

Today, I was teaching my highschool computer class. (I volunteer teach a Wednesday CS class) I wanted to build a Wordle solver so we took a JSON file containing all words in the English language, filtering all 5 letter words out of the file then using it to figure out suggestions for today's Wordle based on letters included, excluded and positions. We got lost, some highschoolers couldn't download files.. It was a hot mess. But it was a neat idea. Finally one kid was like, are the words in the JS file? We dug through the source code and found all the Wordle words. 

Digging through the publically available source code, It seems this might be a babel or webpack generated app. What is interesting is the Wordle is a hard coded list words, indexed by the current day. Inside nytimes.com/games/wordle there is a main.randomChars.js file. Chrome's dev tools will show you them. <br /> <img src="/assets/img/wordle-compiled.png" alt="wordle-compiled" /> 

Today's Wordle was caulk, so if you search for that, you will eventually find a minified array containing all Wordles. The ones for yesterday, tomorrow, and next week. 

Today's was caulk, yesterday's was armoa and tomorrow's will be shake. 

Here's a sampling of some of the wordle's: 

```text
"brake","pluck","craze","gripe","weary","picky","acute","ferry","aside","tapir","troll","unify","rebus","boost","truss","siege","tiger","banal","slump","crank","gorge","query","drink","favor","abbey","tangy","panic","solar","shire","proxy","point","robot","prick","wince","crimp","knoll","sugar","whack","mount","perky","could","wrung","light","those","moist","shard","pleat","aloft","skill","elder","frame","humor","pause","ulcer","ultra","robin","cynic","aroma","caulk","shake"
```

If you want to cheat and see all options, you're welcome to go look at the source code. Or you could just play the game. 

If I were the NyTimes, I'd suggest either at minimum encoding the Wordles or make an API call that returns the wordle of the day. 
