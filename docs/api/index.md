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

!!! info
    - **Responses**:
        - Success: `Image`
        - Failure: `JSON`

### /quote
*Generates images that look like Discord messages.*

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
    
=== "Response (Success)"
    <br>
    <img alt="quote" src="/assets/img/quote.png">

=== "Response (Failure)"
    <br>
    **Empty JSON Body/No JSON Provided**  
    ```json
    {
      "error": true,
      "message": "Invalid or empty JSON Body provided."
    }
    ```
    
    **Malformed JSON or invalid values**  
    ```json
    {
      "error": true,
      "message": "Couldn't generate Image. Make sure the values are valid!"
    }
    ```
    

### /status
*Adds a status icon to the provided Avatar.*

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
    
=== "Response (Success)"
    <br>
    <img alt="status" src="/assets/img/status.png" style="width: 80px; height: 80px;">

=== "Response (Failure)"
    <br>
    **Empty JSON Body/No JSON Provided**  
    ```json
    {
      "error": true,
      "message": "Invalid or empty JSON Body provided."
    }
    ```
    
    **Malformed JSON or invalid values**  
    ```json
    {
      "error": true,
      "message": "Couldn't generate Image. Make sure the values are valid!"
    }
    ```

----

## GET <small>(SFW)</small>
Contains images that are considered safe for work.  
You can access those endpoints through simple `GET` requests.

!!! info
    - **Responses**:
        - Success: `JSON`
        - Failure: `JSON`

### /img/sfw/background/img

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/background/img/gradient_orange.png",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/bite/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/bite/gif/bite_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/blush/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/background/blush/gif/blush_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/cry/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/cry/gif/cry_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/cuddle/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/cuddle/gif/cuddle_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/eevee/:type
`:type` can be either `gif` for gifs or `img` for images.

=== "Response (Success GIF)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/eevee/gif/eevee_001.gif",
      "time": 0
    }
    ```

=== "Response (Success IMG)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/eevee/img/eevee_001.jpg",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/feed/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/feed/gif/feed_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/fluff/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/fluff/gif/fluff_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/holo/img

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/holo/img/holo_001.jpg",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/hug/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/hug/gif/hug_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/icon/img

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/icon/img/holo.png",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/kiss/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/kiss/gif/kiss_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/kitsune/img

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/kitsune/img/kitsune_001.jpg",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/lick/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/lick/gif/lick_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/neko/:type
`:type` can be either `gif` for gifs or `img` for images.

=== "Response (Success GIF)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/neko/gif/neko_001.gif",
      "time": 0
    }
    ```

=== "Response (Success IMG)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/neko/img/neko_001.jpg",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/pat/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/pat/gif/pat_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/poke/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/poke/gif/poke_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/senko/img

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/senko/img/senko_001.jpg",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/slap/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/slap/gif/slap_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/smile/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/smile/gif/smile_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/tail/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/tail/gif/tail_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/sfw/tickle/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/tickle/gif/tickle_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

----

## GET <small>(NSFW)</small>
Contains images that are considered Not Safe for work.  
If you are using those images on Discord, make sure to only share them in Channels marked as NSFW.  
You can access those endpoints through simple `GET` requests.

!!! info
    - **Responses**:
        - Success: `JSON`
        - Failure: `JSON`

### /img/nsfw/anal/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/anal/gif/anal_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/nsfw/blowjob/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/blowjob/gif/blowjob_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/nsfw/cum/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/cum/gif/cum_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/nsfw/fuck/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/fuck/gif/fuck_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/nsfw/neko/:type
`:type` can be either `gif` for gifs or `img` for images.

=== "Response (Success GIF)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/neko/gif/neko_001.gif",
      "time": 0
    }
    ```

=== "Response (Success IMG)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/neko/gif/neko_001.jpg",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/nsfw/pussylick/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/pussylick/gif/pussylick_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/nsfw/solo/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/solo/gif/solo_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/nsfw/threesome_fff/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/threesome_fff/gif/threesome_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/nsfw/threesome_ffm/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/threesome_ffm/gif/threesome_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/nsfw/threesome_mmf/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/threesome_mmf/gif/threesome_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/nsfw/yaoi/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/yaoi/gif/yaoi_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```

### /img/nsfw/yuri/gif

=== "Response (Success)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/yuri/gif/yuri_001.gif",
      "time": 0
    }
    ```

=== "Response (Failure)"
    **Invalid Path (Not an API endpoint)**  
    ```json
    {
      "error": true,
      "message": "Not supported API path"
    }
    ```
    
    **Invalid Path (No images)**  
    ```json
    {
      "error": true,
      "message": "The selected path doesn't contain any images"
    }
    ```
