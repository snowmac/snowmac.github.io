---
layout: post
title: "Automate deleting of Facebook messages"
date: 2024-04-05
categories: javascript chrome console facebook
---

I lothe Facebook Messenger. It lacks a feature I value a lot: bulk delete. Well, I tried to fully automate the click on menu, click delete button then finally click the delete chat button. I even found a script that <a href="https://github.com/mdunham/delete-fb-messages" taget="_blank">does it</a>. The bad news is that script is badly out of date and does not work. But the idea is sound. I found that script had a pull request so I went to check it out.

The script is below, it's within the `()` and I modified it a bit. I wanted to delete marketplace messages and archived messages. Why? Archive goes back 15 years for me. I wanted to rid myself of all of them. Why Market place? I get notifications on 1 year+ items that someone updated and added more detail to. For example firewood, they update the existing listing instead of creating new ones. Very annoying.

To use, open the Chrome console and paste it in, change 'optionsToDelete.archived' to 'optionsToDelete.marketplace' if you want to kill all marketplace items. I only made slight modifications to the script.

Enjoy it!

```javascript
var optionsToDelete = {
  archived: "archived",
  marketplace: "marketplace",
};

var thingToDelete = optionsToDelete.archived;

(function (querySelector) {
  /**
   * Finds and clicks the three-dot menu button to open the chat actions menu.
   * If the button is not found, logs a message indicating that there are no more messages to delete.
   */
  function openChatActionsMenu() {
    var menuButton = window.location.href.includes(thingToDelete)
      ? querySelector('div[aria-label="Menu"]')
      : querySelector('div[aria-label="Menu"]');

    if (menuButton !== null) {
      menuButton.click();
      setTimeout(findDeleteChatButton, 200);
    } else {
      console.log("No messages to delete");
    }
  }

  /**
   * Finds and clicks the "Delete chat" button in the chat actions menu.
   * If the button is not found, logs a message indicating that the delete button was not found.
   */
  function findDeleteChatButton() {
    var deleteButton = Array.from(
      document.querySelectorAll('div[role="menuitem"]')
    ).find(function (element) {
      return element.textContent.includes("Delete chat");
    });

    if (deleteButton !== undefined) {
      deleteButton.click();
      setTimeout(confirmDeleteChat, 200);
    } else {
      console.log("Delete button not found");
    }
  }

  /**
   * Finds and clicks the confirmation button to delete the chat.
   * If the button is not found, logs a message indicating that the confirm button was not found.
   */
  function confirmDeleteChat() {
    var confirmButton = querySelector(
      'div[aria-label="Delete chat"][role="button"]'
    );

    if (confirmButton !== null) {
      confirmButton.click();
      setTimeout(checkForMoreMessages, 600);
    } else {
      console.log("Confirm button not found");
    }
  }

  /**
   * Checks if there are more messages to delete by looking for the three-dot menu button.
   * If the button is found, restarts the process by calling openChatActionsMenu.
   * If the button is not found, logs a message indicating that there are no more messages.
   */
  function checkForMoreMessages() {
    var menuButton = window.location.href.includes(thingToDelete)
      ? querySelector('div[aria-label="Menu"]')
      : querySelector('div[aria-label="Menu"]');

    if (menuButton !== null) {
      setTimeout(openChatActionsMenu, 600);
    } else {
      console.log("No more messages");
    }
  }

  console.log("Deleting messages");
  openChatActionsMenu();
})(function (selector) {
  return document.querySelector(selector);
});
```
