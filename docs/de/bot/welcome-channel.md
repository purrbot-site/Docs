---
title: Einrichten
description: Wie du das Willkommenssystem einrichten kannst.
---

The welcome channel allows you to greet people with a message and image when they join your Discord.

!!! info "Notes"
    Before you set up the channel, make sure you have made the following checks first:
    
    - You have `Manage Server` permission or are the owner of the Discord server.
    - The bot has `Send Messages` and `Attach Files` permission for the channel where it should send the welcome messsages.
    
    For simplicity reasons will the shown commands here use the default prefix (`p.`).  
    If you have set a different prefix, use that instead.

??? youtube "Video Tutorial"
    Here is a video explaining the steps below.
    
    <iframe width="560" height="315" src="https://www.youtube.com/embed/vfhSj-4PF1A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Step 1: Set a channel {: #step-1 }
<!-- md-badge:required -->
<!-- md-badge:default none -->

You first have to set a channel, before you can greet people.  
To do that, run `p.welcome channel set #channel` where `#channel` is the channel you want to use for greeting people.

Reset this using `p.welcome channel reset`

## Step 2: Set a background {: #step-2 }
<!-- md-badge:optional -->
[<!-- md-badge:default color_white -->](welcome-images.md#color_white)

Set a background that will be used on the image.  
The syntax is `p.welcome bg set <background>` where `<background>` is one of the [available backgrounds](welcome-images.md#backgrounds).

Reset this using `p.welcome bg reset`

## Step 3: Set an icon {: #step-3 }
<!-- md-badge:optional -->
[<!-- md-badge:default purr -->](welcome-images.md#purr)

You can set an icon, which is shown on the right side of the image.  
Use `p.welcome icon set <icon>` where `<icon>` is one of the [available icons](welcome-images.md#icons).

Reset this using `p.welcome icon reset`

## Step 4: Set a text color {: #step-4 }
<!-- md-badge:optional -->
<!-- md-badge:default hex:000000 -->

The default font color isn't visible on all backgrounds. For that can you change it with `.welcome color set <color>`.  
`<color>` has to be either `hex:rrggbb`, `rgb:r,g,b` or `random`.

Reset this using `p.welcome color reset`

## Step 5: Set a message {: #step-5 }
<!-- md-badge:optional -->
<!-- md-badge:default Welcome {mention}! -->

You can set your very own welcome message that is shown next to the image.  
To do that run `p.welcome msg set <message>` where `<message>` can be anything you want.  

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

Reset this using `p.welcome msg reset`

## Final Step: Testing {: #final-step }
<!-- md-badge:optional -->
<!-- md-badge:default Saved values -->

You can see the current message and image set by running `p.welcome test`  
This will generate a message similar to the one which would be shown for joining members.
