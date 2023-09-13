---
layout: post
title: "Conversations with an AI: Part 1"
date: 2023-09-12
categories: conversations ai prompt-engineering
---

I might be crazy, but I find that I talk to my computer and they talk back, yes they. I talk to multiple models (I hope my wife isn't jealous), not those kinds of models, but language models. My two favorite companions are Chat GPT 3.5 and Claude 2. I'm getting a local copy of LLama 2, so we'll see how that goes. But since I'm talking to the voices in my computer and not just the voices in my head (joking, eh? Perhaps? Perhaps not?), I thought I'd share what they have to say. The computer voices. 

Every good story and conversation begins with a captivating opening, like one of the authors mental disorders of which consist of multiple voices rambling about how their AI pet will destroy us all. This story begins much in the same way.

# And then there was a prompt

```text
I'm a NodeJS and React developer wanting to build modern web applications leveraging AI with Python? I'm used to NPM, webpack, jest, eslint, package.json, reactjs, expressjs, .... learning a new eco system seems daunting. What tools do you recommend I look at that are most similar to what I've been doing? What will help me quickly get up to speed? I want to work with backend tech to leverage AIs like Llama 2 and OpenAI. 
```

Not the most riveting of prompts but ChatGPT had a really good answer, so much so, I decided to post it here. 

Chat GPT 3.5 Response: 
```text
It's great that you want to leverage AI in your web applications as a Node.js and React developer. Transitioning to Python for AI integration may seem daunting, but it's definitely feasible, especially given your existing development experience. Here are some tools and frameworks to help you get started and transition smoothly:

1. **Python**: Start by learning Python, as it's the primary language for AI and machine learning. Python is relatively easy to pick up, and there are plenty of resources available for developers coming from other programming backgrounds.

2. **Flask or Django**: Since you have experience with Express.js for backend development, Flask or Django can be good options to transition to Python web frameworks. Flask is a micro web framework that's minimalistic and flexible, while Django is a high-level framework that provides many built-in features. You can choose the one that aligns better with your project requirements and personal preferences.

3. **Virtual Environments**: Python has a package manager called `pip`, similar to NPM. You can use virtual environments (e.g., `venv` or `virtualenv`) to manage dependencies for different projects, similar to `package.json`.

4. **AI Libraries and Frameworks**:
   - **TensorFlow and Keras**: These are popular libraries for machine learning and deep learning. They have Python APIs that make it relatively easy to integrate AI models into your applications.
   - **PyTorch**: Another widely used deep learning framework that provides Python support.
   - **scikit-learn**: A user-friendly machine learning library that's great for traditional ML tasks.
   - **OpenAI API**: Since you mentioned OpenAI, they offer Python SDKs for easy integration. You can use their GPT-3 or Llama 2 API for AI-powered features in your apps.

5. **Jupyter Notebooks**: Jupyter is a popular tool for data exploration and development in Python. It's somewhat similar to running code in a REPL, which can be a familiar experience if you've used the Node.js REPL.

6. **Testing and Linting**: Python has its testing and linting tools. For testing, you can use `unittest` or third-party libraries like `pytest`. For linting, you can use tools like `flake8`.

7. **Webpack Alternative**: If you're looking for a build tool similar to Webpack, consider using `Parcel` or `Rollup`. These tools can bundle your Python web application assets.

8. **Eslint Alternative**: For linting in Python, you can use tools like `pylint` or `flake8`. They help maintain code quality similar to ESLint.

9. **Learning Resources**: There are plenty of online courses, tutorials, and books available for learning Python and integrating AI into web applications. Websites like Coursera, edX, and Udemy offer comprehensive courses on these topics.

10. **Git**: If you're not already using it, Git is universal for version control across various languages and platforms. It's essential for collaborative development.

Remember that transitioning to a new technology stack takes time and practice, so be patient with yourself. Start with small projects to get comfortable with the new ecosystem. Also, consider working on projects that combine your existing Node.js and React skills with Python-based AI features gradually. This approach will help you leverage your existing knowledge while learning new concepts.
```

Then to compare and contrast it with it's arch nemesis, Claude 2.0: 

```text
Here are some recommendations for transitioning from NodeJS/React to Python for web development and leveraging AI:

- Learn Flask or Django for the web framework. These are Python equivalents to Express.js in Node. The routing, request/response handling, and middleware concepts are very similar.

- Use Pip and virtual environments for package management. This is similar to NPM for Node. Requirements.txt serves a similar purpose to package.json for defining dependencies. 

- Use Jupyter Notebooks for development. This allows you to write and test code incrementally like a REPL. It's great for experimenting with AI APIs.

- Try PyTorch and TensorFlow for building neural networks and machine learning models. These are the top Python frameworks used with AI.

- Use pytest for testing. It's a popular Python testing framework like Jest in JS.

- Look into Docker for containerization. This helps with dependency management and deployment like Webpack.

- Consider Flask extensions like Flask-RESTful to quickly build REST APIs.

- Check out Celery for background task queueing like you may be used to with Node.

The main adjustment will be around syntax and tooling. But Python has very similar frameworks and capabilities to Node for web dev. The transition should be fairly smooth if you focus on equivalent libraries. The Python ecosystem supports AI development very well.
```

Each tool has their pros and cons, but I like that Claude is more concise then ChatGPT. It doesn't add a bunch of unneccesary text, which for someone who like me... bagel, bagel, bagellll.... sorry what were we talking about? Oh thats right, someone like me who gets distracted like a dog walking through a field of bunny rabbits, I'm very partial to something and someone who can be much more concise. 

A few key take aways from the two: 

1. Flask is a good starting point for ExpressJS lightness and likeness
2. Both mentioned PyTorch and TensorFlow
3. Both mentioned Jupyter Notebooks, which is a data / development IDE 
4. Both talked about Pip and virtual environments. Virtual environments is not something I've heard of within context of a language, so it's neat to explore that concept. 

Claude did a better job of being more concise but omitted some tooling details like webpack and eslint. Open AI answered every question and tech tool mention as if it were a question. It was more detailed and thorough. Having the two in my back pocket is a useful thing to use when I'm trying something new on. 

Why am I considering Python? Well, just because <a href="http://www.adambourg.com/startups/work/life/lessons/learned/2023/09/06/Adventures-in-startups.html">my startup work </a> and co-founder role are finished at the other company, my journey to startup founder and lifestyle entrepreneur are not yet given up just yet. I've got a running list of ideas, and I have more ideas then time. But that doesn't answer the question about Python vs NodeJS. 

# NodeJS vs Python 

Historically there is a performance difference between NodeJS and Python. Python 2 is much slower then Python 3 and even then NodeJS. A lot of this boils down to the fact that NodeJS is non blocking IO, event driven and built specifically for the web as a language. Contrast that with Python that is built as a general purpose language, before the likes of Data Scientists and ML engineers was heavily used by Sys Admins and researchers. 

From my research with NodeJS 20 and Python 3.1, there is a much smaller gap between the two. To the point where unless you're running at scale and all things being the same (They never are), running NodeJS vs Python is more a cultural, organizational and political decision then a technical one. Given an application built on NodeJS, you should keep running it on NodeJS and build services for specific use cases where Python and AI would be easier / better / cheaper / smarter to do in Python. But for a green field project where the creator wants to become an AI expert? Well, then, the choice is clear: Python. 

# What about React? 

While ReactJS, NodeJS, Typescript, REST and GraphQL (VOMIT); have all paid the bills for the last 7 or so years and allowed me to build a good lifestyle, putting those reasons aside, I think that React is over engineered. Many projects in the JS domain qualify for Resume Keyword grabs and do not operate at the best wishes and interests of the underlying client. 

React taught us that the Event Loop and mechanisms behind how the browser works is stupid. That everything UI/UX should be functional, composable and stateful. State should drive everything. Events trigger state changes which then eventually determine what the user sees. Want to show a help box? Control it through an event and state. What to show a modal of text already on the screen? Control it through an event and state. Show where the user missed a question on the form? Control it through an event and state.

.... 

I could write another blog post on the topic, I probably will. My next side project will probably be one of the following: 

1. Svelte based. 
2. VueJS based (still a virtual dom! :( ).
3. A full stack Python MVC app with UI/UX controlled through the server (Like rails but for Python). 
4. A mostly vanilla ish JS app.
5. Low code / No code web app talking to a custom backend.
