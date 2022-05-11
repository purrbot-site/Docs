---
title: API
description: 'Documentation about the ImageAPI located under https://purrbot.site/api'

hide:
  - navigation
  - toc
---

[source]: https://github.com/purrbot-site/ImageAPI
[SimpleDateFormat]: https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html

# API Documentation

The ImageAPI was created as a replacement for your common Image APIs such as nekos.life.  
Endpoints are available to use without any authentication required.

The [Source code][source] is publicly available and contributions are always welcome.

!!! note "Base URL"
    https://purrbot.site/api

## Sections

- [Safe for Work (SFW) Endpoints](#sfw-endpoints)
- [Not Safe for Work (NSFW) Endpoints](#nsfw-endpoints)

----

## Safe for Work (SFW) Endpoints { #sfw-endpoints }

??? api-post "/quote <span class='description'>Generates an image that mimics a Discord message.</span>"
    <h3>Request</h3>
    
    <h4>Type</h4>
    
    :octicons-file-code-24: `application/json`  
    
    <h4>Note</h4>
    
    You must provide an empty JSON body (`{}`) if you want to use the default values.
    
    <h4>Body</h4>
    
    | Name       | Type         | Default                                         | Notes                                |
    | ---------- | ------------ | ----------------------------------------------- | ------------------------------------ |
    | avatar     | String (URL) | https://purrbot.site/assets/img/api/unknown.png |                                      |
    | dateFormat | String       | `dd. MMM yyyy`                                  | Uses [SimpleDateFormat]              |
    | message    | String       | `This is an example message.`                   |                                      |
    | nameColor  | String       | `hex:ffffff`                                    | Supported: `rgb:r,g,b`, `hex:rrggbb` |
    | timestamp  | Integer      | `Current time`                                  |                                      |
    | username   | String       | `Someone`                                       |                                      |
    
    
    ```json title="Example"
    {
      "avatar": "https://cdn.discordapp.com/avatars/204232208049766400/dfaaefa54a2804addb1f494da7aa904d.png",
      "dateFormat": "dd. MMM yyyy",
      "message": "This is an example message.",
      "nameColor": "hex:ffffff",
      "timestamp": 1583708400,
      "username": "Andre_601"
    }
    ```
    
    <h3>Response</h3>
    
    ??? success "200"
    
        <h4>Type</h4>
        
        :octicons-image-24: `image/png`
        
        ![quote](/assets/img/quote.png)
        
    ??? failure "400"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "details": {
            "path": "/api/quote",
            "content-type": ":your-content-type",
            "user-agent": ":your-user-agent"
          },
          "error": true,
          "message": "Received invalid or empty JSON Body."
        }
        ```
        
        --8<-- "api-error-scheme.md"
        
    ??? failure "500"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "details": {
            "path": "/api/quote",
            "content-type": ":your-content-type",
            "user-agent": ":your-user-agent"
          },
          "error": true,
          "message": "Couldn't generate Image. Make sure the values are valid!"
        }
        ```
        
        --8<-- "api-error-scheme.md"

??? api-post "/status <span class='description'>Generates an image that displays an avatar with a Status icon.</span>"
    <h3>Request</h3>
    
    **Type:** :octicons-file-code-24: `application/json`
    
    <h4>Body</h4>
    
    | Name       | Type         | Default                                         | Notes                                                            |
    | ---------- | ------------ | ----------------------------------------------- | ---------------------------------------------------------------- |
    | avatar     | String (URL) | https://purrbot.site/assets/img/api/unknown.png |                                                                  |
    | mobile     | Boolean      | `false`                                         | Changes the icon to a phone. Not used with status `offline`.     |
    | status     | String       | `offline`                                       | Supported: `online`, `idle`, `do_not_disturb`/`dnd` or `offline` |
    
    
    ```json title="Example"
    {
      "avatar": "https://cdn.discordapp.com/avatars/204232208049766400/dfaaefa54a2804addb1f494da7aa904d.png",
      "mobile": false,
      "status": "online"
    }
    ```
    
    <h3>Response</h3>
    
    ??? success "200"
    
        <h4>Type</h4>
        
        :octicons-image-24: `image/png`
        
        ![status](/assets/img/status.png){ width="25%" height="auto" }
        
    ??? failure "400"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "details": {
            "path": "/api/status",
            "content-type": ":your-content-type",
            "user-agent": ":your-user-agent"
          },
          "error": true,
          "message": "Received invalid or empty JSON Body."
        }
        ```
        
        --8<-- "api-error-scheme.md"
        
    ??? failure "500"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "details": {
            "path": "/api/status",
            "content-type": ":your-content-type",
            "user-agent": ":your-user-agent"
          },
          "error": true,
          "message": "Couldn't generate Image. Make sure the values are valid!"
        }
        ```
        
        --8<-- "api-error-scheme.md"

----

??? api-get "/img/sfw/background/img <span class='description'>Returns a randomly selected Welcome Background Image.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/background/img/color_black.png",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/bite/gif <span class='description'>Returns a randomly selected Bite Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/bite/gif/bite_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/blush/gif <span class='description'>Returns a randomly selected Blush Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/blush/gif/blush_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/comfy/gif <span class='description'>Returns a randomly selected Comfy Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/comfy/gif/comfy_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/cry/gif <span class='description'>Returns a randomly selected Cry Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/cry/gif/cry_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/cuddle/gif <span class='description'>Returns a randomly selected Cuddle Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/cuddle/gif/cuddle_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/dance/gif <span class='description'>Returns a randomly selected Dance Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/dance/gif/dance_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/eevee/{type} <span class='description'>Returns a randomly selected Eevee Image/Gif.</span>"
    <h3>Parameters</h3>
    
    | Name | Description                                          |
    | ---- | ---------------------------------------------------- |
    | type | The Image type to return. Supported: `gif` or `img`. |
    
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example Gif"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/eevee/gif/eevee_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
        ```json title="Example Image"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/eevee/img/eevee_001.jpg",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/feed/gif <span class='description'>Returns a randomly selected Feeding Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/feed/gif/feed_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/fluff/gif <span class='description'>Returns a randomly selected Blush Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/fluff/gif/fluff_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/holo/img <span class='description'>Returns a randomly selected Image of Holo from 'Spice and Wolf'</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/holo/img/holo_001.jpg",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/hug/gif <span class='description'>Returns a randomly selected hugging Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/hug/gif/hug_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/icon/img <span class='description'>Returns a randomly selected Welcome Icon.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/icon/img/holo.jpg",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/kiss/gif <span class='description'>Returns a randomly selected kissing Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/kiss/gif/kiss_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/kitsune/img <span class='description'>Returns a randomly selected Kitsune (Fox Girl) Image.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/kitsune/img/kitsune_001.jpg",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/lick/gif <span class='description'>Returns a randomly selected licking Gif</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/lick/gif/lick_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/neko/{type} <span class='description'>Returns a randomly selected Neko (Cat Girl) Gif or Image.</span>"
    <h3>Parameters</h3>
    
    | Name | Description                                          |
    | ---- | ---------------------------------------------------- |
    | type | The Image type to return. Supported: `gif` or `img`. |
    
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example Gif"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/neko/gif/neko_001.gif",
          "time": 0
        }
        ```
        
        ```json title="Example Image"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/neko/img/neko_001.jpg",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/okami/img <span class='description'>Returns a randomly selected Okami (Wolf Girl) Image.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/okami/img/okami_001.jpg",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/pat/gif <span class='description'>Returns a randomly selected patting Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/pat/gif/pat_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/poke/gif <span class='description'>Returns a randomly selected poking Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/poke/gif/poke_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/senko/img <span class='description'>Returns a randomly selected Image of Senko-San.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/senko/img/senko_001.jpg",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/slap/gif <span class='description'>Returns a randomly selected slapping Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/slap/gif/slap_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/smile/gif <span class='description'>Returns a randomly selected smiling Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/smile/gif/smile_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/tail/gif <span class='description'>Returns a randomly selected tail wagging Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/tail/gif/tail_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/tickle/gif <span class='description'>Returns a randomly selected tickling Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/tickle/gif/tickle_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/list/sfw/{path} <span class='description'>Lists all found images of the specified {path}</span>"
    <h3>Parameters</h3>
    
    | Name | Description                                                                                       |
    | ---- | ------------------------------------------------------------------------------------------------- |
    | path | The path to the image folder. Available paths are the same as with all the `/api/img/` endpoints. |
    
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "links": [
            "https://purrbot.site/img/sfw/background/img/color_black.png",
            "https://purrbot.site/img/sfw/background/img/color_blue.png",
            "https://purrbot.site/img/sfw/background/img/color_blurple.png",
            "https://purrbot.site/img/sfw/background/img/color_green.png",
            "https://purrbot.site/img/sfw/background/img/color_grey.png",
            "https://purrbot.site/img/sfw/background/img/color_red.png",
            "https://purrbot.site/img/sfw/background/img/color_white.png",
            "https://purrbot.site/img/sfw/background/img/gradient.png",
            "https://purrbot.site/img/sfw/background/img/gradient_blue.png",
            "https://purrbot.site/img/sfw/background/img/gradient_dark_red.png",
            "https://purrbot.site/img/sfw/background/img/gradient_green.png",
            "https://purrbot.site/img/sfw/background/img/gradient_orange.png",
            "https://purrbot.site/img/sfw/background/img/gradient_red.png",
            "https://purrbot.site/img/sfw/background/img/rainbow.png"
          ],
          "time": 0
        }
        ```
        
        <h4>Scheme</h4>
        
        - `error`: Boolean  
          Always returns false for successful requests.
        - `links`: Array  
          Array of Strings representing URLs to the Images/Gifs found in the directory.
        - `time`: Integer  
          Time in milliseconds it took for the API to process the request.
    
    --8<-- "api-img-errors.md"

----

## Not Safe for Work (NSFW) Endpoints { #nsfw-endpoints }

??? api-get "/img/nsfw/anal/gif <span class='description'>Returns a randomly selected Anal-Sex Gif</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/anal/gif/anal_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/blowjob/gif <span class='description'>Returns a randomly selected blowjob Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/blowjob/gif/blowjob_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/cum/gif <span class='description'>Returns a randomly selected cumming Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/cum/gif/cum_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/fuck/gif <span class='description'>Returns a randomly selected Sex Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/fuck/gif/fuck_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/neko/{type} <span class='description'>Returns a randomly selected NSFW Neko (Cat Girl) Gif or Image.</span>"
    <h3>Parameters</h3>
    
    | Name | Description                                         |
    | ---- | --------------------------------------------------- |
    | type | The Image type to return. Supported: `gif` or `img` |
    
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example Gif"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/neko/gif/neko_001.gif",
          "time": 0
        }
        ```
        
        ```json title="Example Image"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/neko/img/neko_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/pussylick/gif <span class='description'>Returns a randomly selected pussy licking Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/pussylick/gif/pussylick_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/solo/gif <span class='description'>Returns a randomly selected Gif of a female masturbating.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/solo/gif/solo_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/threesome_fff/gif <span class='description'>Returns a randomly selected Threesome Gif (Females only).</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/threesome_fff/gif/threesome_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/threesome_ffm/gif <span class='description'>Returns a randomly selected Threesome Gif (2 Females, 1 Male).</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/threesome_ffm/gif/threesome_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/threesome_mmf/gif <span class='description'>Returns a randomly selected Threesome Gif (1 Female, 2 Males).</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/threesome_mmf/gif/threesome_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/yaoi/gif <span class='description'>Returns a randomly selected Yaoi (Gay Hentai) Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/yaoi/gif/yaoi_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/yuri/gif <span class='description'>Returns a randomly selected Yuri (Lesbian Hentai) Gif.</span>"
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/yuri/gif/yuri_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/list/nsfw/{path} <span class='description'>Lists all found images of the specified {path}</span>"
    <h3>Parameters</h3>
    
    | Name | Description                                                                                       |
    | ---- | ------------------------------------------------------------------------------------------------- |
    | path | The path to the image folder. Available paths are the same as with all the `/api/img/` endpoints. |
    
    <h3>Response</h3>
    
    ??? success "200"
        --8<-- "api-response-header.md"
        
        ```json title="Example"
        {
          "error": false,
          "links": [
            "https://purrbot.site/img/nsfw/anal/gif/anal_001.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_002.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_003.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_004.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_005.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_006.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_007.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_008.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_009.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_010.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_011.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_012.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_013.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_014.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_015.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_016.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_017.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_018.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_019.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_020.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_021.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_022.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_023.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_024.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_025.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_026.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_027.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_028.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_029.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_030.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_031.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_032.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_033.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_034.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_035.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_036.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_037.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_038.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_039.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_040.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_041.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_042.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_043.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_044.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_045.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_046.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_047.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_048.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_049.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_050.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_051.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_052.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_053.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_054.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_055.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_056.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_057.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_058.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_059.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_060.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_061.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_062.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_063.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_064.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_065.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_066.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_067.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_068.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_069.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_070.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_071.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_072.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_073.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_074.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_075.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_076.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_077.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_078.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_079.gif",
            "https://purrbot.site/img/nsfw/anal/gif/anal_080.gif"
          "time": 0
        }
        ```
        
        <h4>Scheme</h4>
        
        - `error`: Boolean  
          Always returns false for successful requests.
        - `links`: Array  
          Array of Strings representing URLs to the Images/Gifs found in the directory.
        - `time`: Integer  
          Time in milliseconds it took for the API to process the request.
    
    --8<-- "api-img-errors.md"
