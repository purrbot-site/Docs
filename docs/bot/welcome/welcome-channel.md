---
title: Setup the Welcome System
description: How to setup the Welcome System.
---

[patreon]: https://patreon.com/andre_601

The welcome channel allows you to greet people with a message and image when they join your Discord.

!!! info "Notes"
    Before you set up the channel, make sure you have made the following checks first:
    
    - You have `Manage Server` permission or are the owner of the Discord server.
    - The bot has `Send Messages` and `Attach Files` permission for the channel where it should send the welcome messsages.

??? youtube "Video Tutorial"
    Here is a video explaining the steps below.
    
    <iframe width="560" height="315" src="https://www.youtube.com/embed/vfhSj-4PF1A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Step 1: Set a channel {: #step-1 }
You first need to set a channel. To do this, run `/welcome channel <textchannel: channel>` where `<textchannel: channel>` is the Text channel you want to use.  
Please make sure that the bot has sufficient permissions for the provided channel to work.

You can reset this with `/welcome reset channel`

## Step 2: Set a background {: #step-2 }
Now should you set a welcome background through `/welcome background <string: background>` where `<string: background>` should be the name of the background you want to use.

By default is [`color_white`](/bot/welcome-images#color_white) used but you can set any [available background](/bot/welcome-images) you like.  
As a Server booster can you also set the [`booster`](/bot/welcome-images#booster-background) background and as a [Tier 2 or Tier 3 Patreon][patreon] can you use [any background you like](/bot/welcome-images#custom-background).

You can reset this with `/welcome reset background`

## Step 3: Set an icon {: #step-3 }
Next step is to set an icon using `/welcome icon <string: icon>` where `<string: icon>` is the name of the icon you want to use.

By default is [`purr`](/bot/welcome-images#purr) used but you can set any [available icon](/bot/welcome-images) you like.  
As a Server booster can you also set the [`booster`](/bot/welcome-images#booster-icon) icon and as a [Tier 2 or Tier 3 Patreon][patreon] can you use [any icon you like](/bot/welcome-images#custom-icon).

You can reset this with `/welcome reset icon`

## Step 4: Set a text color {: #step-4 }
Not every background works well with the font colour used.  
That's why you can also change the font colour using `/welcome color <string: color>` where `<string: color>` should be either `hex:rrggbb` (example: `hex:ffffff`), `rgb:r,g,b` (example: `rgb:255,255,255`) or `random`.

You can reset this with `/welcome reset color`

## Step 5: Set a message {: #step-5 }
What is a welcome-system without a way to set your own message?  
With `/welcome message <string: message>`, where `<string: message>` is the message you want to use, can you set you set your very own message to display alongside the welcome image!  
You can use the below listed placeholders to display different information for each new user.

You can reset this with `/welcome reset message`

### Placeholders

| Placeholder:                                | Description:                                                                | Example Output: |
| ------------------------------------------- | --------------------------------------------------------------------------- | --------------- |
| `{count}` / `{members}`                     | The current amount of members on the Discord server.                        | 1000            |
| `{count_formatted}` / `{members_formatted}` | The current amount of members on the Discord server, but formatted.         | 1,000           |
| `{guild}` / `{server}`                      | The name of the server.                                                     | SomeDiscord     |
| `{mention}`                                 | Mention of the user that joined the server.                                 | @SomeUser       |
| `{name}` / `{username}`                     | The name of the user that joined the server.                                | SomeUser        |
| `{c_mention:<id>}`                          | A mention of the provided channel ID. Works with text and voice.            | #SomeChannel    |
| `{c_name:<id>}`                             | The name of the provided channel ID. Works with any channel and categories. | SomeChannel     |
| `{r_mention:<id>}`                          | A mention of the provided role ID.                                          | @SomeRole       |
| `{r_name:<id>}`                             | The name of the provided role ID.                                           | SomeRole        |
| `{tag}`                                     | The tag of the user that joined the server.                                 | SomeUser#1234   |

## Final Step: Testing {: #final-step }
All that is left is to test your work. For that simply run `/welcome test` and the bot should respond with the message and image you defined shortly after.
