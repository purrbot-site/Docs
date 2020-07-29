[SimpleDateFormat]: https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html

# API Documentation
The ImageAPI was created to be a replacement for the nekos.life API in the bot \*Purr\*.  
It is publicly available to use.

Since version 1.2.0 of this API can you also find the endpoints of the former PurrBotAPI in this one.  
The API is [open source](https://github.com/purrbot-site/ImageAPI) and contributions are always welcome.

!!! note "Base URL"
    https://purrbot.site/api

## POST
These API endpoints can only be used through `POST` requests.

### /quote
*Generates images that look like Discord messages.*

!!! info
    - **Responses:
        - Success: `Image`
        - Failure: `JSON`

#### Fields

=== "avatar"
    **Type**: String  
    **Default**: https://purrbot.site/assets/img/api/unknown.png
    
    **Description**:  
    The URL of the avatar to display in the image. The image will be resized to 217x217 pixels.
    
=== "dateFormat"
    **Type**: String  
    **Default**: `dd. MMM yyyy hh:mm:ss zzz`
    
    **Description**:  
    The format in which the date should be displayed.  
    This uses the [SimpleDateFormat] from Java.
    
=== "message"
    **Type**: String  
    **Default**: `Some message`
    
    **Description**:  
    The actual message that should be displayed.  
    Note that this will **NOT** render markdown and can only render a few selected emojis (No Discord emotes).
    
=== "nameColor"
    **Type**: String  
    **Default**: `hex:ffffff`
    
    **Description**:  
    The color in which the username should be displayed.  
    Supported are `hex:rrggbb`, `rgb:r,g,b` or the raw Color value.
    
=== "timestamp"
    **Type**: Number  
    **Default**: Current time of the request
    
    **Description**:  
    The date of the message as epoch milliseconds.
    
=== "username"
    **Type**: String  
    **Default**: `Someone`
    
    **Description**:  
    The username to display.

#### Example

=== "Request"
    <br>
    This request was made on march, 9th 2020.  
    ```json
    {
      "avatar": "https://cdn.discordapp.com/avatars/204232208049766400/dfaaefa54a2804addb1f494da7aa904d.png",
      "message": "This is an example message.",
      "nameColor": "hex:ffffff",
      "dateFormat": "dd. MMM yyyy",
      "username": "Andre_601"
    }
    ```
    
=== "Response"
    <br>
    <img alt="quote" src="/assets/img/quote.png">

### /status
*Adds a status icon to the provided Avatar.*

!!! info
    - **Responses:
        - Success: `Image`
        - Failure: `JSON`

#### Fields

=== "avatar"
    **Type**: String  
    **Default**: https://purrbot.site/assets/img/api/unknown.png
    
    **Description**:  
    The URL of the avatar to display in the image. The image will be resized to 950x950 pixels.
    
=== "mobile"
    **Type**: Boolean  
    **Default**: `false`
    
    **Description**:  
    Wether the user is on mobile. `true` will change the status icon to that used to indicate mobile users on Discord (Small smartphone).
    
=== "status"
    **Type**: String  
    **Default**: `offline`
    
    **Description**:  
    The status to display with the icon.  
    Available are `online`, `idle`, `do_not_disturb` (or `dnd`), `streaming` and `offline`.

#### Example

=== "Request"
    <br>
    ```json
    {
      "avatar": "https://cdn.discordapp.com/avatars/204232208049766400/dfaaefa54a2804addb1f494da7aa904d.png",
      "status": "online"
    }
    ```
    
=== "Response"
    <br>
    <img alt="status" src="/assets/img/status.png" style="width: 80px; height: 80px;">

## GET <small>(SFW (Safe for work) endpoints)</small>
Contains images that are considered safe for work.  
You can access those endpoints through simple `GET` requests.

!!! info
    - **Responses:
        - Success: `JSON`
        - Failure: `JSON`

### /img/sfw/background/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/background/img/gradient_orange.png",
  "time": 0
}
```

### /img/sfw/bite/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purbot.site/img/sfw/bite/gif/bite_001.gif",
  "time": 0
}
```

### /img/sfw/cuddle/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/cuddle/gif/cuddle_001.gif",
  "time": 0
}
```

### /img/sfw/eevee/:type
`:type` can be either `gif` for gifs or `img` for images.

Example responses:

=== "Image"
    ```json
    {
      "code": 200,
      "link": "https://purrbot.site/img/sfw/eevee/img/eevee_001.jpg",
      "time": 0
    }
    ```
=== "Gif"
    ```json
    {
      "code": 200,
      "link": "https://purrbot.site/img/sfw/eevee/gif/eevee_001.gif",
      "time": 0
    }
    ```

### /img/sfw/feed/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/feed/gif/feed_001.gif",
  "time": 0
}
```

### /img/sfw/holo/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/holo/img/holo_001.jpg",
  "time": 0
}
```

### /img/sfw/hug/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/hug/gif/hug_001.gif",
  "time": 0
}
```

### /img/sfw/icon/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/icon/img/purr.png",
  "time": 0
}
```

### /img/sfw/kiss/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/kiss/gif/kiss_001.gif",
  "time": 0
}
```

### /img/sfw/kitsune/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/kitsune/img/kitsune_001.jpg",
  "time": 0
}
```

### /img/sfw/lick/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/lick/gif/lick_001.gif",
  "time": 0
}
```

### /img/sfw/neko/:type
`:type` can be either `gif` for gifs or `img` for images.

Example responses:

=== "Image"
    ```json
    {
      "code": 200,
      "link": "https://purrbot.site/img/sfw/neko/img/neko_001.jpg",
      "time": 0
    }
    ```
=== "Gif"
    ```json
    {
      "code": 200,
      "link": "https://purrbot.site/img/sfw/neko/gif/neko_001.gif",
      "time": 0
    }
    ```

### /img/sfw/pat/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/pat/gif/pat_001.gif",
  "time": 0
}
```

### /img/sfw/poke/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/poke/gif/poke_001.gif",
  "time": 0
}
```

### /img/sfw/senko/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/senko/img/senko_001.jpg",
  "time": 0
}
```

### /img/sfw/slap/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/slap/gif/slap_001.gif",
  "time": 0
}
```

### /img/sfw/tail/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/tail/gif/tail_001.gif",
  "time": 0
}
```

### /img/sfw/tickle/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/tickle/gif/tickle_001.gif",
  "time": 0
}
```

----

## GET <small>(NSFW (Not safe for work) endpoints)</small>
Contains images that are considered Not Safe for work.  
If you are using those images on Discord, make sure to only share them in Channels marked as NSFW.  
You can access those endpoints through simple `GET` requests.

!!! info
    - **Responses:
        - Success: `JSON`
        - Failure: `JSON`

### /img/nsfw/anal/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/anal/gif/anal_001.gif",
  "time": 0
}
```

### /img/nsfw/blowjob/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/blowjob/gif/blowjob_001.gif",
  "time": 0
}
```

### /img/nsfw/cum/gif
Example response:
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/cum/gif/cum_001.gif",
  "time": 0
}
```

### /img/nsfw/fuck/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/fuck/gif/fuck_001.gif",
  "time": 0
}
```

### /img/nsfw/neko/:type
`:type` can be either `gif` for gifs or `img` for images.

Example responses:

=== "Image"
    ```json
    {
      "code": 200,
      "link": "https://purrbot.site/img/nsfw/neko/img/neko_001.jpg",
      "time": 0
    }
    ```
=== "Gif"
    ```json
    {
      "code": 200,
      "link": "https://purrbot.site/img/nsfw/neko/gif/neko_001.gif",
      "time": 0
    }
    ```

### /img/nsfw/pussylick/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/pussylick/gif/pussylick_001.gif",
  "time": 0
}
```

### /img/nsfw/solo/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/solo/gif/solo_001.gif",
  "time": 0
}
```

### /img/nsfw/threesome_fff/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/threesome_fff/gif/threesome_001.gif",
  "time": 0
}
```

### /img/nsfw/threesome_ffm/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/threesome_ffm/gif/threesome_001.gif",
  "time": 0
}
```

### /img/nsfw/threesome_mmf/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/threesome_mmf/gif/threesome_001.gif",
  "time": 0
}
```

### /img/nsfw/yuri/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/yuri/gif/yuri_001.gif",
  "time": 0
}
```

----

## Failed requests
The API can return one of two error responses, depending on which one is the case.

=== "403: Not supported API path"
    When you connect to an API path which does not exist (e.g. `/api/img/doesntexist`) will this error response be displayed.
    
    ```json
    {
      "code": 403,
      "message": "Not supported API path",
      "time": 0
    }
    ```
    
=== "403: The selected directory doesn't contain any images"
    If the provided path doesn't contain any images, will this error be displayed.
    
    ```json
    {
      "code": 403,
      "message": "The selected directory doesn't contain any images",
      "time": 0
    }
    ```
=== "403: Invalid or empty JSON body provided."
    Your request didn't contain any JSON (Not even just `{}`) or the JSON was invalid.  
    Common issues of invalid JSON are missing commas or similar.
    
    ```json
    {
      "code": 403,
      "message": Invalid or empty JSON body provided.",
      "time": 0
    }
    ```

=== "500: Couldn't generate image. Make sure the values are valid!"
    The API was unable to generate an image from the provided JSON.  
    This is often the case when things like the Avatar URL lead to an invalid page.
    
    ```json
    {
      "code": 500,
      "message": "Couldn't generate image. Make sure the values are valid!"
    }
    ```
