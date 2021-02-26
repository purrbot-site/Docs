---
title: Setup the Welcome System
description: How to setup the Welcome System.
---

The welcome channel allows you to greet people with a message and image when they join your Discord.

!!! info "Notes"
    Before you set up the channel, make sure you have made the following checks first:
    
    - You have `Manage Server` permission or are the owner of the Discord server.
    - The bot has `Send Messages` and `Attach Files` permission for the channel where it should send the welcome messsages.
    
    For simplicity reasons will the shown commands here use the default prefix (`p.`).  
    If you have set a different prefix, use that instead.

??? "Video Tutorial"
    Here is a video explaining the steps below.
    
    <iframe width="560" height="315" src="https://www.youtube.com/embed/vfhSj-4PF1A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Step 1: Set a channel {: #step-1 }
> **Required step?** Yes  
> **Default**: `None`

You first have to set a channel, before you can greet people.  
To do that, run `p.welcome channel set #channel` where `#channel` is the channel you want to use for greeting people.

Reset this using `p.welcome channel reset`

## Step 2: Set a background {: #step-2 }
> **Required step?** No  
> **Default**: [`color_white`](/bot/welcome-images#color_white)

Set a background that will be used on the image.  
The syntax is `p.welcome bg set <background>` where `<background>` is one of the [available backgrounds](/bot/welcome-images#backgrounds).

Reset this using `p.welcome bg reset`

## Step 3: Set an icon {: #step-3 }
> **Required step?** No  
> **Default**: [`purr`](/bot/welcome-images#purr)

You can set an icon, which is shown on the right side of the image.  
Use `p.welcome icon set <icon>` where `<icon>` is one of the [available icons](/bot/welcome-images#icons).

Reset this using `p.welcome icon reset`

## Step 4: Set a text color {: #step-4 }
> **Required step?** No  
> **Default**: `hex:000000`

The default font color isn't visible on all backgrounds. For that can you change it with `.welcome color set <color>`.  
`<color>` has to be either `hex:rrggbb`, `rgb:r,g,b` or `random`.

Reset this using `p.welcome color reset`

## Step 5: Set a message {: #step-5 }
> **Required step?** No  
> **Default**: `Welcome {mention}!`

You can set your very own welcome message that is shown next to the image.  
To do that run `p.welcome msg set <message>` where `<message>` can be anything you want.  
You can also use placeholders in the message:

- `{count}` / `{members}` The member count of the Discord (e.g. 1000).
- `{count_formatted}` / `{members_formatted}` The member count of the Discord but formatted (e.g. 1,000).
- `{guild}` / `{server}` The name of the Discord.
- `{mention}` The joined user as a mention.
- `{name}` / `{username}` The name of the joined user.
- `{c_mention:<id>}` A channel-mention. `<id>` has to be a Text Channel id (Other channel types won't work).
- `{c_name:<id>}` The name of a channel. `<id>` has to be a channel id.
- `{r_mention:<id>}` A role-mention. `<id>` has to be a role id.
- `{r_name:<id>}` The name of a role. `<id>` has to be a role id.
- `{tag}` The tag (username and discriminator) of the user.

Reset this using `p.welcome msg reset`

## Final Step: Testing {: #final-step }
> **Required step?** No  
> **Default**: `Uses saved values`

You can see the current message and image set by running `p.welcome test`  
This will generate a message similar to the one which would be shown for joining members.
