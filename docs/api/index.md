---
title: API
description: Detailed information about the ImageAPI.
---

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
    - **Responses**:
        - Success: `Image`
        - [Failure: `JSON`](#apiquote)

#### Fields {: #fields-quote }

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

#### Example {: #example-quote }

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
    ![quote](/assets/img/quote.png)
    

### /status
*Adds a status icon to the provided Avatar.*

!!! info
    - **Responses**:
        - Success: `Image`
        - [Failure: `JSON`](#apistatus)

#### Fields {: #fields-status }

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

#### Example {: #example-status }

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
    ![status](/assets/img/status.png){: width="80" }

----

## GET <small>(SFW)</small>
Contains images that are considered safe for work.  
You can access those endpoints through simple `GET` requests.

!!! info
    - **Responses**:
        - Success: `JSON`
        - [Failure: `JSON`](#apiimg)

### [/img/sfw/background/img](https://purrbot.site/api/img/sfw/background/img) {: #img-sfw-background-img }
Returns a Random [Welcome Background](/bot/welcome-images#backgrounds).

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/background/img/color_black.png",
  "time": 0
}
```

### [/img/sfw/bite/gif](https://purrbot.site/api/img/sfw/bite/gif) {: #img-sfw-bite-gif }
Returns a random Bite Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/bite/gif/bite_001.gif",
  "time": 0
}
```

### [/img/sfw/blush/gif](https://purrbot.site/api/img/sfw/blush/gif) {: #img-sfw-blush-gif }
Returns a random blush Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/blush/gif/blush_001.gif",
  "time": 0
}
```

### [/img/sfw/cry/gif](https://purrbot.site/api/img/sfw/cry/gif) {: #img-sfw-cry-gif }
Returns a random Cry Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/cry/gif/cry_001.gif",
  "time": 0
}
```

### [/img/sfw/cuddle/gif](https://purrbot.site/api/img/sfw/cuddle/gif) {: #img-sfw-cuddle-gif }
Returns a random Cuddle Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/cuddle/gif/cuddle_001.gif",
  "time": 0
}
```

### [/img/sfw/dance/gif](https://purrbot.site/api/img/sfw/dance/gif) {: #img-sfw-dance-gif }
Returns a random Dance Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/dance/gif/dance_001.gif",
  "time": 0
}
```

### [/img/sfw/eevee/:type](https://purrbot.site/api/img/sfw/eevee/gif) {: #img-sfw-eevee-type }
Returns either a random Eevee Image or Gif.  
`:type` can be either `gif` for gifs or `img` for images.

=== "Response (GIF)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/eevee/gif/eevee_001.gif",
      "time": 0
    }
    ```

=== "Response (IMG)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/eevee/img/eevee_001.jpg",
      "time": 0
    }
    ```

### [/img/sfw/feed/gif](https://purrbot.site/api/img/sfw/feed/gif) {: #img-sfw-feed-gif }
Returns a random Feeding Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/feed/gif/feed_001.gif",
  "time": 0
}
```

### [/img/sfw/fluff/gif](https://purrbot.site/api/img/sfw/fluff/gif) {: #img-sfw-fluff-gif }
Returns a random Fluffing Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/fluff/gif/fluff_001.gif",
  "time": 0
}
```

### [/img/sfw/holo/img](https://purrbot.site/api/img/sfw/holo/img) {: #img-sfw-holo-img }
Returns a random Image of Holo (Spice & Wolf).

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/holo/img/holo_001.gif",
  "time": 0
}
```

### [/img/sfw/hug/gif](https://purrbot.site/api/img/sfw/hug/gif) {: #img-sfw-hug-gif }
Returns a random Hug Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/hug/gif/hug_001.gif",
  "time": 0
}
```

### [/img/sfw/icon/img](https://purrbot.site/api/img/sfw/icon/img) {: #img-sfw-icon-img }
Returns a random [Welcome Icon](/bot/welcome-images#icons)

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/icon/img/holo.png",
  "time": 0
}
```

### [/img/sfw/kiss/gif](https://purrbot.site/api/img/sfw/kiss/gif) {: #img-sfw-kiss-gif }
Returns a random Kiss Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/kiss/gif/kiss_001.gif",
  "time": 0
}
```

### [/img/sfw/kitsune/img](https://purrbot.site/api/img/sfw/kitsune/img) {: #img-sfw-kitsune-img }
Returns a random Image of a Kitsune (Fox girl).

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/kitsune/img/kitsune_001.png",
  "time": 0
}
```

### [/img/sfw/lick/gif](https://purrbot.site/api/img/sfw/lick/gif) {: #img-sfw-lick-gif }
Returns a random Lick Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/lick/gif/lick_001.gif",
  "time": 0
}
```

### [/img/sfw/neko/:type](https://purrbot.site/api/img/sfw/neko/gif) {: #img-sfw-neko-type }
Returns either a random Neko Image or Gif.  
`:type` can be either `gif` for gifs or `img` for images.

=== "Response (GIF)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/neko/gif/neko_001.gif",
      "time": 0
    }
    ```

=== "Response (IMG)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/neko/img/neko_001.jpg",
      "time": 0
    }
    ```

### [/img/sfw/okami/img](https://purrbot.site/api/img/sfw/okami/img) {: #img-sfw-okami-img }
Returns a random Image of an Okami (Wolf girl).

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/okami/img/okami_001.jpeg",
  "time": 0
}
```

### [/img/sfw/pat/gif](https://purrbot.site/api/img/sfw/pat/gif) {: #img-sfw-pat-gif }
Returns a random Pat Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/pat/gif/pat_001.gif",
  "time": 0
}
```

### [/img/sfw/poke/gif](https://purrbot.site/api/img/sfw/poke/gif) {: #img-sfw-poke-gif }
Returns a random Poke Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/poke/gif/poke_001.gif",
  "time": 0
}
```

### [/img/sfw/senko/img](https://purrbot.site/api/img/sfw/senko/img) {: #img-sfw-senko-img }
Returns a random Image of Senko-San.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/senko/img/senko_001.png",
  "time": 0
}
```

### [/img/sfw/slap/gif](https://purrbot.site/api/img/sfw/slap/gif) {: #img-sfw-slap-gif }
Returns a random Slap Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/slap/gif/slap_001.gif",
  "time": 0
}
```

### [/img/sfw/smile/gif](https://purrbot.site/api/img/sfw/smile/gif) {: #img-sfw-smile-gif }
Returns a random Smile Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/smile/gif/smile_001.gif",
  "time": 0
}
```

### [/img/sfw/tail/gif](https://purrbot.site/api/img/sfw/tail/gif) {: #img-sfw-tail-gif }
Returns a random Tail wagging Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/tail/gif/tail_001.gif",
  "time": 0
}
```

### [/img/sfw/tickle/gif](https://purrbot.site/api/img/sfw/tickle/gif) {: #img-sfw-tickle-gif }
Returns a random Tickle Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/sfw/tickle/gif/tickle_001.gif",
  "time": 0
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
        - [Failure: `JSON`](#apiimg)

### [/img/nsfw/anal/gif](https://purrbot.site/api/img/nsfw/anal/gif) {: #img-nsfw-anal-gif }
Returns a random Anal-sex Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/nsfw/anal/gif/anal_001.gif",
  "time": 0
}
```

### [/img/nsfw/blowjob/gif](https://purrbot.site/api/img/nsfw/blowjob/gif) {: #img-nsfw-blowjob-gif }
Returns a random Blowjob Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/nsfw/blowjob/gif/blowjob_001.gif",
  "time": 0
}
```

### [/img/nsfw/cum/gif](https://purrbot.site/api/img/nsfw/cum/gif) {: #img-nsfw-cum-gif }
Returns a random Cumming Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/nsfw/cum/gif/cum_001.gif",
  "time": 0
}
```

### [/img/nsfw/fuck/gif](https://purrbot.site/api/img/nsfw/fuck/gif) {: #img-nsfw-fuck-gif }
Returns a random Sex Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/nsfw/fuck/gif/fuck_001.gif",
  "time": 0
}
```

### [/img/nsfw/neko/:type](https://purrbot.site/api/img/nsfw/neko/gif) {: #img-nsfw-neko-type }
Returns either a random lewd Neko Image or Gif.  
`:type` can be either `gif` for gifs or `img` for images.

=== "Response (GIF)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/neko/gif/neko_001.gif",
      "time": 0
    }
    ```

=== "Response (IMG)"
    ```json
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/neko/gif/neko_001.jpg",
      "time": 0
    }
    ```

### [/img/nsfw/pussylick/gif](https://purrbot.site/api/img/nsfw/pussylick/gif) {: #img-nsfw-pussylick-gif }
Returns a random Pussy licking Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/nsfw/pussylick/gif/pussylick_001.gif",
  "time": 0
}
```

### [/img/nsfw/solo/gif](https://purrbot.site/api/img/nsfw/solo/gif) {: #img-nsfw-solo-gif }
Returns a random Girl masturbating Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/nsfw/solo/gif/solo_001.gif",
  "time": 0
}
```

### [/img/nsfw/threesome_fff/gif](https://purrbot.site/api/img/nsfw/threesome_fff/gif) {: #img-nsfw-threesome_fff-gif }
Returns a random Threesome (only Female) Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/nsfw/threesome_fff/gif/threesome_001.gif",
  "time": 0
}
```

### [/img/nsfw/threesome_ffm/gif](https://purrbot.site/api/img/nsfw/threesome_ffm/gif) {: #img-nsfw-threesome_ffm-gif }
Returns a random Threesome (2 Female, 1 Male) Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/nsfw/threesome_ffm/gif/threesome_001.gif",
  "time": 0
}
```

### [/img/nsfw/threesome_mmf/gif](https://purrbot.site/api/img/nsfw/threesome_mmf/gif) {: #img-nsfw-threesome_mmf-gif }
Returns a random Threesome (2 Male, 1 Female) Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/nsfw/threesome_mmf/gif/threesome_001.gif",
  "time": 0
}
```

### [/img/nsfw/yaoi/gif](https://purrbot.site/api/img/nsfw/yaoi/gif) {: #img-nsfw-yaoi-gif }
Returns a Random Yaoi (Gay) sex Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/nsfw/yaoi/gif/yaoi_001.gif",
  "time": 0
}
```

### [/img/nsfw/yuri/gif](https://purrbot.site/api/img/nsfw/yuri/gif) {: #img-nsfw-yuri-gif }
Returns a random Yuri (Lesbian) sex Gif.

```json
{
  "error": false,
  "link": "https://purrbot.site/img/nsfw/yuri/gif/yuri_001.gif",
  "time": 0
}
```

----

## Failed Requests
The API will return a JSON body whenever a request failed.  
An error is returned for the following cases:

!!! note "Note"
    Following placeholders are used in the below examples and may look different per-request:
    
    - `:content-type` The `Content-Type` set for the Request (i.e. `application/json`).
    - `:user-agent` The `User-Agent` used for the Request (i.e. `Chrome`).
    - `:path` The path targeted by the Request (i.e. `sfw/cuddle/gif`)

### /api/quote {: #api-quote }

=== "Empty JSON Body/No JSON"
    **Status-Code**: 403  
    ```json
    {
      "details": {
        "path": "/api/quote",
        "content-type": ":content-type",
        "user-agent": ":user-agent"
      },
      "error": true,
      "message": "Received invalid or empty JSON Body."
    }
    ```

=== "Malformed JSON/Invalid Values"
    **Status-Code**: 500  
    ```json
    {
      "details": {
        "path": "/api/quote",
        "content-type": ":content-type",
        "user-agent": ":user-agent"
      },
      "error": true,
      "message": "Couldn't generate Image. Make sure the values are valid!"
    }
    ```

### /api/status {: #api-status }

=== "Empty JSON Body/No JSON"
    ```json
    {
      "details": {
        "path": "/api/status",
        "content-type": ":content-type",
        "user-agent": ":user-agent"
      },
      "error": true,
      "message": "Received invalid or empty JSON Body."
    }
    ```

=== "Malformed JSON/Invalid Values"
    ```json
    {
      "details": {
        "path": "/api/status",
        "content-type": ":content-type",
        "user-agent": ":user-agent"
      },
      "error": true,
      "message": "Couldn't generate Image. Make sure the values are valid!"
    }
    ```

### /api/img/* {: #api-img }

=== "Invalid Path (No API endpoint)"
    **Status-Code**: 403  
    ```json
    {
      "details": {
        "path": "/api/img/:path",
        "content-type": ":content-type",
        "user-agent": ":user-agent"
      },
      "error": true,
      "message": "The selected API path is not supported!"
    }
    ```

=== "No Images available"
    **Status-Code**: 403  
    ```json
    {
      "details": {
        "path": "/api/img/:path",
        "content-type": ":content-type",
        "user-agent": ":user-agent"
      },
      "error": true,
      "message": "The selected API path does not contain any images!"
    }
    ```
