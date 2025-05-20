---
layout: post
title: "Scraping YouTube Transcripts for AI Summarization with JavaScript"
date: 2025-05-20
categories: javascript youtube web-scraping ai
---

# Scraping YouTube Transcripts for AI Summarization with JavaScript

Hey there! I recently tackled a neat challenge: pulling the transcript from a YouTube video and cleaning it up to feed into an AI like ChatGPT or Grok for a quick summary. The goal was to grab all the text from a `segments-container` element on YouTube’s page, strip out the noise (like timestamps and extra spaces), and copy it to the clipboard for easy pasting into an AI tool. To get there, I needed to click a couple of elements to reveal the transcript. Here’s how I pulled it off with a slick vanilla JavaScript script.

## The Mission

The plan was to extract the full transcript text from a YouTube video’s `segments-container` element, which holds the caption data. YouTube buries this behind a couple of clicks: an element with the text "...more" to expand the description and another with `aria-label="Show transcript"` to display the transcript. The text needed to be clean—no newlines, numbers, colons (like timestamps), or excessive spaces—so it’s ready to paste into an AI for summarization. The script had to be robust, handling cases where elements might be missing, and it needed to run automatically when pasted into the browser console.

## Why I Went with a Custom Script

When I set out to scrape YouTube transcripts, I could’ve leaned on third-party services, APIs, or something like a Greasemonkey script, but I wasn’t feeling those options. Third-party services often come with strings attached—subscriptions, rate limits, or sketchy data practices that make you wonder who’s peeking at your info. APIs, like YouTube’s official one, are powerful but require setup, authentication, and sometimes fees, which felt like overkill for a quick transcript grab. Greasemonkey scripts? They’re cool for automation, but installing a browser extension or user script can be a hassle, and you never know if some random script is sneaking in spyware or tracking junk.

Instead, I wanted something lean, self-contained, and under my control—a pure vanilla JavaScript snippet I could paste into the console and run on the spot. No dependencies, no external servers, just a few lines of code doing exactly what I need: click a couple of elements, clean the text, and copy it for AI summarization. This approach keeps things fast, transparent, and spyware-free, so I can trust what’s happening every step of the way. Plus, it’s easy to tweak if YouTube changes their layout. Total win.

## How It Works

Here’s the breakdown of the script, step by step:

### Step 1: Clicking the "...more" Element 🔍

First, we need to expand the video description to access the transcript option. I used `document.querySelectorAll('*')` to search all elements for one with the exact text "...more". It could be a button, div, or anything else, so we keep it flexible. If found, we click it and log a confirmation. If not, we note it in the console and move on—no big deal, the transcript might still be accessible.

### Step 2: Waiting for the Page to Catch Up ⏳

Clicking "...more" might trigger some dynamic content loading, so we pause for 3 seconds using `setTimeout`. This gives YouTube’s DOM time to update before we look for the next element.

### Step 3: Clicking the “Show transcript” Element 📜

Next, we hunt for an element with `aria-label="Show transcript"`, again using a broad selector (`[aria-label="Show transcript"]`) to catch any element type. If it’s there, we click it and log the action. If it’s missing, we log a warning and keep going, as the transcript might already be visible in some cases.

### Step 4: Brief Pause for Transcript Loading ⏱️

After clicking “Show transcript,” we wait 1 second to ensure the transcript loads into the `segments-container`. This short delay helps avoid grabbing incomplete data.

### Step 5: Extracting and Cleaning the Text 🧹

Now we target the `segments-container` element by its ID. If it’s not found, we log an error and stop. If it’s there, we use `textContent` to grab all the text, then clean it with regex:

- `[\n\r0-9:]+` removes newlines, carriage returns, numbers, and colons (goodbye, timestamps!).
- `\s+` collapses multiple spaces into a single space.
- A final `trim()` ensures no stray whitespace at the start or end.

### Step 6: Copying to the Clipboard 📋

The cleaned text gets copied to the clipboard using `navigator.clipboard.writeText()`. We log a success message if it works or an error if it fails (e.g., due to a non-secure context like HTTP). The text is also returned to the console for manual copying if needed.

### Step 7: Error Handling 🛡️

The script is wrapped in `try-catch` blocks at every step to keep things smooth. If the "...more" element fails or is missing, we proceed to “Show transcript.” If that fails, we still try to grab the text. This ensures we get as far as possible, even on quirky pages.

## The Code

Below is the full script. It’s an Immediately Invoked Function Expression (IIFE), so it runs the moment you paste it into your browser’s console. Just open a YouTube video, paste this in the console, and the cleaned transcript will be copied to your clipboard, ready for AI summarization.

```javascript
(function cleanSegmentsText() {
  try {
    const moreElement = Array.from(document.querySelectorAll("*")).find(
      (el) => el.textContent.trim() === "...more" && el instanceof HTMLElement
    );
    if (moreElement) {
      moreElement.click();
      console.log('Clicked the "...more" element');
    } else {
      console.warn('Element with text "...more" not found, proceeding to next step');
    }
    setTimeout(() => {
      try {
        const transcriptElement = Array.from(document.querySelectorAll('[aria-label="Show transcript"]')).find(
          (el) => el instanceof HTMLElement
        );
        if (transcriptElement) {
          transcriptElement.click();
          console.log('Clicked the "Show transcript" element');
        } else {
          console.warn('Element with aria-label="Show transcript" not found, proceeding to extract text');
        }
        setTimeout(() => {
          try {
            const container = document.getElementById("segments-container");
            if (!container) {
              console.error('Element with id "segments-container" not found, cannot extract text');
              return "";
            }
            const text = container.textContent
              .trim()
              .replace(/[\n\r0-9:]+/g, "")
              .replace(/\s+/g, " ")
              .trim();
            navigator.clipboard
              .writeText(text)
              .then(() => {
                console.log("Text copied to clipboard successfully!");
              })
              .catch((err) => {
                console.error("Failed to copy text to clipboard:", err.message);
              });
            return text;
          } catch (err) {
            console.error("Error extracting or cleaning text from segments-container:", err.message);
            return "";
          }
        }, 1000);
      } catch (err) {
        console.warn('Error clicking "Show transcript" element:', err.message, "Proceeding to extract text");
        setTimeout(() => {
          try {
            const container = document.getElementById("segments-container");
            if (!container) {
              console.error('Element with id "segments-container" not found, cannot extract text');
              return "";
            }
            const text = container.textContent
              .trim()
              .replace(/[\n\r0-9:]+/g, "")
              .replace(/\s+/g, " ")
              .trim();
            navigator.clipboard
              .writeText(text)
              .then(() => {
                console.log("Text copied to clipboard successfully!");
              })
              .catch((err) => {
                console.error("Failed to copy text to clipboard:", err.message);
              });
            return text;
          } catch (err) {
            console.error("Error extracting or cleaning text from segments-container:", err.message);
            return "";
          }
        }, 1000);
      }
    }, 3000);
  } catch (err) {
    console.warn('Error clicking "...more" element:', err.message, "Proceeding to next step");
    setTimeout(() => {
      try {
        const transcriptElement = Array.from(document.querySelectorAll('[aria-label="Show transcript"]')).find(
          (el) => el instanceof HTMLElement
        );
        if (transcriptElement) {
          transcriptElement.click();
          console.log('Clicked the "Show transcript" element');
        } else {
          console.warn('Element with aria-label="Show transcript" not found, proceeding to extract text');
        }
        setTimeout(() => {
          try {
            const container = document.getElementById("segments-container");
            if (!container) {
              console.error('Element with id "segments-container" not found, cannot extract text');
              return "";
            }
            const text = container.textContent
              .trim()
              .replace(/[\n\r0-9:]+/g, "")
              .replace(/\s+/g, " ")
              .trim();
            navigator.clipboard
              .writeText(text)
              .then(() => {
                console.log("Text copied to clipboard successfully!");
              })
              .catch((err) => {
                console.error("Failed to copy text to clipboard:", err.message);
              });
            return text;
          } catch (err) {
            console.error("Error extracting or cleaning text from segments-container:", err.message);
            return "";
          }
        }, 1000);
      } catch (err) {
        console.warn('Error clicking "Show transcript" element:', err.message, "Proceeding to extract text");
        setTimeout(() => {
          try {
            const container = document.getElementById("segments-container");
            if (!container) {
              console.error('Element with id "segments-container" not found, cannot extract text');
              return "";
            }
            const text = container.textContent
              .trim()
              .replace(/[\n\r0-9:]+/g, "")
              .replace(/\s+/g, " ")
              .trim();
            navigator.clipboard
              .writeText(text)
              .then(() => {
                console.log("Text copied to clipboard successfully!");
              })
              .catch((err) => {
                console.error("Failed to copy text to clipboard:", err.message);
                console.log(text);
              });
            return text;
          } catch (err) {
            console.error("Error extracting or cleaning text from segments-container:", err.message);
            return "";
          }
        }, 1000);
      }
    }, 3000);
  }
})();
```

## Why It’s Solid

This script is built to handle YouTube’s quirks. It doesn’t care if the "...more" or “Show transcript” elements are buttons, links, or random divs—it’ll find and click them. If either is missing, it keeps going, ensuring you still get the transcript if it’s already visible. The `try-catch` blocks catch any weird errors (like a click failing due to page restrictions), and the delays (3 seconds and 1 second) give YouTube time to load the transcript.

The regex cleanup makes the text AI-ready by ditching timestamps and formatting junk, so you can paste it straight into ChatGPT or Grok for a clean summary. If the clipboard copy fails (e.g., you’re not on HTTPS), you’ll still see the text in the console to grab manually.

## Tips for Use

- **Run It**: Open a YouTube video, pop open the console (F12 or right-click > Inspect > Console), paste the script, and hit Enter. The transcript should be copied to your clipboard.
- **AI Summarization**: Paste the text into ChatGPT, Grok, or your favorite AI tool and ask for a summary. For example, try a prompt like: “Summarize this transcript in 100 words.”
- **Troubleshooting**: Check the console logs for clues if something goes wrong. If the delays are off (e.g., transcript doesn’t load in time), you might need to bump up the 3000ms or 1000ms waits. If the elements have different text or attributes, let me know, and I can tweak the selectors.
- **Clipboard Permission Issue**: If you see an error like "Failed to copy text to clipboard: The request is not allowed by the user agent or the platform in the current context," it’s likely because the page isn’t on HTTPS or you denied clipboard permissions. Make sure you’re on a secure YouTube page (https://www.youtube.com). If prompted, allow clipboard access. Worst case, the cleaned text still shows in the console, so you can copy it manually.

## What’s Next?

This script is a great starting point, but you could level it up. If YouTube’s loading times vary, you could replace `setTimeout` with a polling loop to wait for `segments-container` to update. Or, if you’re summarizing a bunch of videos, you could turn this into a browser extension for one-click scraping. Got ideas for more features? Drop a comment, and let’s keep the conversation going!

Thanks for reading, and happy scraping!
