---
title: API
description: Detailed information about the ImageAPI.

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

??? api-post "/quote"
    Generates an image that mimics a Discord message.
    
    <h3>Request</h3>
    
    **Type:** :octicons-file-code-24: `application/json`  
    **Note:** All Options are optional. You still need to provide an empty JSON Object (`{}`) on the request.
    
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
        **Type:** :octicons-image-24: `image/png`
        
        ![quote](/assets/img/quote.png)
        
    ??? failure "400"
        **Type:** :octicons-file-code-24: `application/json`
        
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
        
    ??? failure "500"
        **Type:** :octicons-file-code-24: `application/json`
        
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

??? api-post "/status"
    Generates an image that displays an avatar with a Status icon.
    
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
        **Type:** :octicons-image-24: `image/png`
        
        ![status](/assets/img/status.png)
        
    ??? failure "400"
        **Type:** :octicons-file-code-24: `application/json`
        
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
        
    ??? failure "500"
        **Type:** :octicons-file-code-24: `application/json`
        
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

----

??? api-get "/img/sfw/background/img"
    Returns a randomly selected [Welcome Background Image](/bot/welcome-images#backgrounds)
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/background/img/color_black.png",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/bite/gif"
    Returns a randomly selected Bite Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/bite/gif/bite_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/blush/gif"
    Returns a randomly selected Blush Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/blush/gif/blush_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/comfy/gif"
    Returns a randomly selected Comfy Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/comfy/gif/comfy_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/cry/gif"
    Returns a randomly selected Cry Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/cry/gif/cry_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/cuddle/gif"
    Returns a randomly selected Cuddle Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/cuddle/gif/cuddle_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/dance/gif"
    Returns a randomly selected Dance Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/dance/gif/dance_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/eevee/{type}"
    Returns a randomly selected Eevee Image/Gif.
    
    <h3>Parameters</h3>
    
    | Name | Description                                          |
    | ---- | ---------------------------------------------------- |
    | type | The Image type to return. Supported: `gif` or `img`. |
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
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

??? api-get "/img/sfw/feed/gif"
    Returns a randomly selected Feeding Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/feed/gif/feed_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/fluff/gif"
    Returns a randomly selected Blush Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/fluff/gif/fluff_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/holo/img"
    Returns a randomly selected Image of Holo from "Spice and Wolf".
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/holo/img/holo_001.jpg",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/hug/gif"
    Returns a randomly selected Hug Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/hug/gif/hug_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
        
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/icon/img"
    Returns a randomly selected [Welcome Icon](/bot/welcome-images#icons).
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/icon/img/holo.jpg",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/kiss/gif"
    Returns a randomly selected Kissing Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/kiss/gif/kiss_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/kitsune/img"
    Returns a randomly selected Kitsune (Fox Girl) Image.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/kitsune/img/kitsune_001.jpg",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/lick/gif"
    Returns a randomly selected Licking Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/lick/gif/lick_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/neko/{type}"
    Returns a randomly selected Neko Gif or Image.
    
    <h3>Parameters</h3>
    
    | Name | Description                                          |
    | ---- | ---------------------------------------------------- |
    | type | The Image type to return. Supported: `gif` or `img`. |
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
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

??? api-get "/img/sfw/okami/img"
    Returns a randomly selected Okami (Wolf Girl) Image.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/okami/img/okami_001.jpg",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/pat/gif"
    Returns a randomly selected patting Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/pat/gif/pat_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/poke/gif"
    Returns a randomly selected poking Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/poke/gif/poke_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/senko/img"
    Returns a randomly selected Image from Senko-San.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/senko/img/senko_001.jpg",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/slap/gif"
    Returns a randomly selected slapping Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/slap/gif/slap_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/smile/gif"
    Returns a randomly selected smiling Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/smile/gif/smile_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/tail/gif"
    Returns a randomly selected Tail wagging Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/tail/gif/tail_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/sfw/tickle/gif"
    Returns a randomly selected tickling Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/sfw/tickle/gif/tickle_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/list/sfw/{path}"
    Returns a list of all images from the provided `{path}`.
    
    <h3>Parameters</h3>
    
    | Name | Description                                                                                       |
    | ---- | ------------------------------------------------------------------------------------------------- |
    | path | The path to the image folder. Available paths are the same as with all the `/api/img/` endpoints. |
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

----

## Not Safe for Work (NSFW) Endpoints { #nsfw-endpoints }

??? api-get "/img/nsfw/anal/gif"
    Returns a randomly selected Anal-Sex Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/anal/gif/anal_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/blowjob/gif"
    Returns a randomly selected Blowjob Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/blowjob/gif/blowjob_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/cum/gif"
    Returns a randomly selected Cumming Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/cum/gif/cum_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/fuck/gif"
    Returns a randomly selected Sex Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/fuck/gif/fuck_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/neko/{type}"
    Returns a randomly selected NSFW Neko Gif or Image.
    
    <h3>Parameters</h3>
    
    | Name | Description                                         |
    | ---- | --------------------------------------------------- |
    | type | The Image type to return. Supported: `gif` or `img` |
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
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

??? api-get "/img/nsfw/pussylick/gif"
    Returns a randomly selected Pussy licking Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/pussylick/gif/pussylick_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/solo/gif"
    Returns a randomly selected Gif of a Female masturbating.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/solo/gif/solo_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/threesome_fff/gif"
    Returns a randomly selected Threesome Gif with just females.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/threesome_fff/gif/threesome_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/threesome_ffm/gif"
    Returns a randomly selected Threesome Gif with 2 females and 1 male.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/threesome_ffm/gif/threesome_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/threesome_mmf/gif"
    Returns a randomly selected Threesome Gif with 2 male and 1 female.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/threesome_mmf/gif/threesome_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/yaoi/gif"
    Returns a randomly selected Yaoi (Gay Hentai) Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/yaoi/gif/yaoi_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/img/nsfw/yuri/gif"
    Returns a randomly selected Yuri (Lesbian Hentai) Gif.
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/yuri/gif/yuri_001.gif",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"

??? api-get "/list/nsfw/{path}"
    Returns a list of all images from the provided `{path}`
    
    <h3>Parameters</h3>
    
    | Name | Description                                                                                       |
    | ---- | ------------------------------------------------------------------------------------------------- |
    | path | The path to the image folder. Available paths are the same as with all the `/api/img/` endpoints. |
    
    <h3>Response</h3>
    
    ??? success "200"
        **Type:** :octicons-file-code-24: `application/json`
        
        ```json title="Example"
        {
          "error": false,
          "link": "https://purrbot.site/img/nsfw/",
          "time": 0
        }
        ```
        
        --8<-- "api-img-success-scheme.md"
    
    --8<-- "api-img-errors.md"