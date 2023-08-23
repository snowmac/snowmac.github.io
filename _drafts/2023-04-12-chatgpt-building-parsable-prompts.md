---
layout: post
title: "chatgpt building parsable prompts"
date: 2023-04-12
categories: chatgpt api ai 
---

I recently started working on a side project where we're using prompts we engineer to generate responses that users can edit, the edits are fed into the Chat GPT call and the cycle continues until we get a final result. Parsing it proved to be harder then expected, but we're going to expore techniques we discovered to make parsing really easy. 

In writing this blogpost, I decided to give Chat GPT a prompt: ```What is the best way to engineer prompts that can easily be parsed?```

It gave me some really clear and concise replies: 

```markdown 
To engineer prompts that can easily be parsed, there are several best practices you can follow:

1. Use clear and concise language: Avoid using overly complicated language or technical jargon. Instead, use simple, easy-to-understand language that clearly conveys the meaning of the prompt.
2. Be specific: Clearly state what information you are looking for and what format you expect it to be in. For example, if you are asking for a date, specify the date format (e.g. MM/DD/YYYY or DD/MM/YYYY).
3. Use structured data: Whenever possible, use structured data formats such as JSON, XML, or CSV to make it easier for the parser to extract information.
4. Use consistent formatting: Use consistent formatting for all prompts to make it easier for the parser to recognize and extract information.
5. Provide examples: Provide examples of valid responses to help the user understand the expected format and content.
6. Test thoroughly: Test your prompts with a variety of inputs to ensure they can be parsed accurately and reliably.

By following these best practices, you can create prompts that are easy to parse and help ensure the accuracy and consistency of the data you collect.
```

All of the above make sense. Lets build a few sample prompts for a hypothetical application where we want to help aid buyers of large consumer products decide on the specific item to buy and then give them informed questions to help them when they're at the store make an informed decision. Let's start with a car. 

Prompt: 

```As a buyer a of a car, what are the top 5 things I should be concerned about when purchasing a new or used car for my growing family? ```

Response: 

```markdown
As an AI language model, I can provide you with the top 5 things you should consider when purchasing a new or used car for your growing family:

1. Safety features: The safety of your family should be your top priority when purchasing a car. Look for cars that have advanced safety features such as anti-lock brakes, electronic stability control, airbags, rearview cameras, blind-spot monitoring, and automatic emergency braking.
2. Size and space: A growing family needs more space, so consider the size of the car and make sure it has enough space to accommodate everyone comfortably, including car seats, strollers, and luggage.
3. Reliability: You want a car that is reliable and won't break down frequently, especially with a growing family. Look for cars with good reliability ratings from sources such as Consumer Reports and JD Power.
4. Fuel economy: With a growing family, you will likely be driving more, so fuel economy is an important factor to consider. Look for cars with good gas mileage or consider hybrid or electric vehicles to save money on fuel costs.
5. Budget: Consider the overall cost of the car, including the purchase price, financing, insurance, and maintenance costs. Make sure the car fits within your budget and won't cause financial strain for your family.

By considering these factors, you can help ensure that you choose a safe, reliable, and comfortable car for your growing family.
```

Prompt: 

```Can you format your response as json?```

Response: 

```markdown 
Certainly, here's an example of how my response could be formatted in JSON:

```json
{
   "top_5_concerns": [
      {
         "concern": "Safety features",
         "description": "The safety of your family should be your top priority when purchasing a car. Look for cars that have advanced safety features such as anti-lock brakes, electronic stability control, airbags, rearview cameras, blind-spot monitoring, and automatic emergency braking."
      },
      {
         "concern": "Size and space",
         "description": "A growing family needs more space, so consider the size of the car and make sure it has enough space to accommodate everyone comfortably, including car seats, strollers, and luggage."
      },
      {
         "concern": "Reliability",
         "description": "You want a car that is reliable and won't break down frequently, especially with a growing family. Look for cars with good reliability ratings from sources such as Consumer Reports and JD Power."
      },
      {
         "concern": "Fuel economy",
         "description": "With a growing family, you will likely be driving more, so fuel economy is an important factor to consider. Look for cars with good gas mileage or consider hybrid or electric vehicles to save money on fuel costs."
      },
      {
         "concern": "Budget",
         "description": "Consider the overall cost of the car, including the purchase price, financing, insurance, and maintenance costs. Make sure the car fits within your budget and won't cause financial strain for your family."
      }
   ]
}
```

```

prompt: ```how many chat gpt tokens did it use?```

response: ```I used 54 Chat GPT tokens to generate the JSON response.```

The first thing we get back is 5 items, budget, fuel economy, reliability, size and safety.  Lets expand on this query

prompt: 

```I have a young child in a car seat, I need a car that is larger then the Honda HRV we have now but is low to the ground so it's easy to load and get into. I need a SUV or larger sedan. Safety is important, but my budget is $25,000 or less. I also drive a lot, so spaciousness and fuel efficiency are important. Can you generate a table of 10 possible cars that fit the above criteria?```