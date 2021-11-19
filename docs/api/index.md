---
title: API
description: Detailed information about the ImageAPI.
---

[def_avatar]: https://purrbot.site/assets/img/api/unknown.png
[SimpleDateFormat]: https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html

# API Documentation
The ImageAPI was created to be a replacement for the nekos.life API in the bot \*Purr\*.  
It is publicly available to use.

Since version 1.2.0 of this API can you also find the endpoints of the former PurrBotAPI in this one.  
The API is [open source](https://github.com/purrbot-site/ImageAPI) and contributions are always welcome.

!!! note "Base URL"
    https://purrbot.site/api

## POST
The below API endpoints require you to make a `POST` request to them. a default `GET` request will automatically redirect to the respective documentation (this page).

To get more information about a value, click the :material-numeric-1-circle: **Number Icon** next to the value to get a text box with useful information such as type and default value.

### /quote
*Generates images that look like Discord messages.*

=== "Request Body"
    ```js title="JSON Body Example"
    {
      "avatar": "https://cdn.discordapp.com/avatars/204232208049766400/dfaaefa54a2804addb1f494da7aa904d.png", // (1)
      "dateFormat": "dd. MMM yyyy", // (2)
      "message": "This is an example message.", // (3)
      "nameColor": "hex:ffffff", // (4)
      "timestamp": 1583708400, // (5)
      "username": "Andre_601" // (6)
    }
    ```

    1.  **Type:** String  
        **Default:** [`https://purrbot.site/assets/img/api/unknown.png`][def_avatar]  
        This has to be a direct URL to an image.
    2.  **Type:** String  
        **Default:** `dd. MMM yyyy hh:mm:yyyy`  
        Sets the format in which the timestamp should be formatted.  
        This uses the [SimpleDateFormat] provided by Java.
    3.  **Type:** String  
        **Default:** `Some message`  
        The message that should be displayed.  
        Due to multiple limitations are formatting options (i.e. `**bold**`) NOT supported!
    4.  **Type:** String  
        **Default:** `hex:ffffff`  
        Sets the colour in which the username should be displayed.  
        Supported formats are `hex:rrggbb`, `rgb:r,g,b` or the raw colour value.
    5.  **Type:** Number  
        **Default:** *Current time of request*  
        The Epoch millis timestamp which will be used together with the `dateFormat` to display the actual date.
    6.  **Type:** String  
        **Default:** Someone  
        The username to display.

=== "Success"
    **Type:** :octicons-image-24: `Image`  
    **Example:**  
    ![quote](/assets/img/quote.png)

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### /status
*Adds a status icon to the provided Avatar.*

=== "Request Body"
    ```js title="JSON Body Example"
    {
      "avatar": "https://cdn.discordapp.com/avatars/204232208049766400/dfaaefa54a2804addb1f494da7aa904d.png", // (1)
      "mobile": false, // (2)
      "status": "online" // (3)
    }
    ```
    
    1.  **Type:** String  
        **Default:** [`https://purrbot.site/assets/img/api/unknown.png`][def_avatar]  
        This has to be a direct URL to an image.
    2.  **Type:** Boolean  
        **Default:** `false`  
        Will display a mobile phone icon instead of the usual indicators when set to `true`.
    3.  **Type:** String  
        **Default:** `offline`  
        Set the status to display as icon. Supported are `online`, `idle`, `do_not_disturb`/`dnd` and `offline`.

=== "Success"
    **Type:** :octicons-image-24: `Image`  
    **Example:**  
    ![status](/assets/img/status.png){ width="80" }

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

----

## GET <small>(SFW)</small>
Contains images that are considered safe for work.  
You can access those endpoints through simple `GET` requests.

### [/img/sfw/background/img](https://purrbot.site/api/img/sfw/background/img) { #img-sfw-background-img }
Returns a Random [Welcome Background](/bot/welcome-images#backgrounds).

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/background/img/color_black.png",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/bite/gif](https://purrbot.site/api/img/sfw/bite/gif) { #img-sfw-bite-gif }
Returns a random Bite Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/bite/gif/bite_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/blush/gif](https://purrbot.site/api/img/sfw/blush/gif) { #img-sfw-blush-gif }
Returns a random blush Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/blush/gif/blush_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/cry/gif](https://purrbot.site/api/img/sfw/cry/gif) { #img-sfw-cry-gif }
Returns a random Cry Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/cry/gif/cry_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/cuddle/gif](https://purrbot.site/api/img/sfw/cuddle/gif) { #img-sfw-cuddle-gif }
Returns a random Cuddle Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/cuddle/gif/cuddle_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/dance/gif](https://purrbot.site/api/img/sfw/dance/gif) { #img-sfw-dance-gif }
Returns a random Dance Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/dance/gif/dance_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/eevee/:type](https://purrbot.site/api/img/sfw/eevee/gif) { #img-sfw-eevee-type }
Returns either a random Eevee Image or Gif.  
`:type` can be either `gif` for gifs or `img` for images.

=== "Response (GIF)"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/eevee/gif/eevee_001.gif",
      "time": 0
    }
    ```

=== "Response (IMG)"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/eevee/img/eevee_001.jpg",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/feed/gif](https://purrbot.site/api/img/sfw/feed/gif) { #img-sfw-feed-gif }
Returns a random Feeding Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/feed/gif/feed_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/fluff/gif](https://purrbot.site/api/img/sfw/fluff/gif) { #img-sfw-fluff-gif }
Returns a random Fluffing Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/fluff/gif/fluff_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/holo/img](https://purrbot.site/api/img/sfw/holo/img) { #img-sfw-holo-img }
Returns a random Image of Holo (Spice & Wolf).

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/holo/img/holo_001.jpg",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/hug/gif](https://purrbot.site/api/img/sfw/hug/gif) { #img-sfw-hug-gif }
Returns a random Hug Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/hug/gif/hug_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/icon/img](https://purrbot.site/api/img/sfw/icon/img) { #img-sfw-icon-img }
Returns a random [Welcome Icon](/bot/welcome-images#icons)

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/icon/img/holo.png",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/kiss/gif](https://purrbot.site/api/img/sfw/kiss/gif) { #img-sfw-kiss-gif }
Returns a random Kiss Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/kiss/gif/kiss_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/kitsune/img](https://purrbot.site/api/img/sfw/kitsune/img) { #img-sfw-kitsune-img }
Returns a random Image of a Kitsune (Fox girl).

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/kitsune/img/kitsune_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/lick/gif](https://purrbot.site/api/img/sfw/lick/gif) { #img-sfw-lick-gif }
Returns a random Lick Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/lick/gif/lick_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/neko/:type](https://purrbot.site/api/img/sfw/neko/gif) { #img-sfw-neko-type }
Returns either a random Neko Image or Gif.  
`:type` can be either `gif` for gifs or `img` for images.

=== "Response (GIF)"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/neko/gif/neko_001.gif",
      "time": 0
    }
    ```

=== "Response (IMG)"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/neko/img/neko_001.jpg",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/okami/img](https://purrbot.site/api/img/sfw/okami/img) { #img-sfw-okami-img }
Returns a random Image of an Okami (Wolf girl).

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/okami/img/okami_001.jpg",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/pat/gif](https://purrbot.site/api/img/sfw/pat/gif) { #img-sfw-pat-gif }
Returns a random Pat Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/pat/gif/pat_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/poke/gif](https://purrbot.site/api/img/sfw/poke/gif) { #img-sfw-poke-gif }
Returns a random Poke Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/poke/gif/poke_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/senko/img](https://purrbot.site/api/img/sfw/senko/img) { #img-sfw-senko-img }
Returns a random Image of Senko-San.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/senko/img/senko_001.jpg",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/slap/gif](https://purrbot.site/api/img/sfw/slap/gif) { #img-sfw-slap-gif }
Returns a random Slap Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/slap/gif/slap_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/smile/gif](https://purrbot.site/api/img/sfw/smile/gif) { #img-sfw-smile-gif }
Returns a random Smile Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/smile/gif/smile_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/tail/gif](https://purrbot.site/api/img/sfw/tail/gif) { #img-sfw-tail-gif }
Returns a random Tail wagging Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/tail/gif/tail_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/sfw/tickle/gif](https://purrbot.site/api/img/sfw/tickle/gif) { #img-sfw-tickle-gif }
Returns a random Tickle Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/sfw/tickle/gif/tickle_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

----

## GET <small>(NSFW)</small>
Contains images that are considered Not Safe for work.  
If you are using those images on Discord, make sure to only share them in Channels marked as NSFW.  
You can access those endpoints through simple `GET` requests.

### [/img/nsfw/anal/gif](https://purrbot.site/api/img/nsfw/anal/gif) { #img-nsfw-anal-gif }
Returns a random Anal-sex Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/anal/gif/anal_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/nsfw/blowjob/gif](https://purrbot.site/api/img/nsfw/blowjob/gif) { #img-nsfw-blowjob-gif }
Returns a random Blowjob Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/blowjob/gif/blowjob_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/nsfw/cum/gif](https://purrbot.site/api/img/nsfw/cum/gif) { #img-nsfw-cum-gif }
Returns a random Cumming Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/cum/gif/cum_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/nsfw/fuck/gif](https://purrbot.site/api/img/nsfw/fuck/gif) { #img-nsfw-fuck-gif }
Returns a random Sex Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/fuck/gif/fuck_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/nsfw/neko/:type](https://purrbot.site/api/img/nsfw/neko/gif) { #img-nsfw-neko-type }
Returns either a random lewd Neko Image or Gif.  
`:type` can be either `gif` for gifs or `img` for images.

=== "Response (GIF)"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/neko/gif/neko_001.gif",
      "time": 0
    }
    ```

=== "Response (IMG)"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/neko/img/neko_001.jpg",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/nsfw/pussylick/gif](https://purrbot.site/api/img/nsfw/pussylick/gif) { #img-nsfw-pussylick-gif }
Returns a random Pussy licking Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/pussylick/gif/pussylick_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/nsfw/solo/gif](https://purrbot.site/api/img/nsfw/solo/gif) { #img-nsfw-solo-gif }
Returns a random Girl masturbating Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/solo/gif/solo_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/nsfw/threesome_fff/gif](https://purrbot.site/api/img/nsfw/threesome_fff/gif) { #img-nsfw-threesome_fff-gif }
Returns a random Threesome (only Female) Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/threesome_fff/gif/threesome_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/nsfw/threesome_ffm/gif](https://purrbot.site/api/img/nsfw/threesome_ffm/gif) { #img-nsfw-threesome_ffm-gif }
Returns a random Threesome (2 Female, 1 Male) Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/threesome_ffm/gif/threesome_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/nsfw/threesome_mmf/gif](https://purrbot.site/api/img/nsfw/threesome_mmf/gif) { #img-nsfw-threesome_mmf-gif }
Returns a random Threesome (2 Male, 1 Female) Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/threesome_mmf/gif/threesome_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/nsfw/yaoi/gif](https://purrbot.site/api/img/nsfw/yaoi/gif) { #img-nsfw-yaoi-gif }
Returns a Random Yaoi (Gay) sex Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/yaoi/gif/yaoi_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

### [/img/nsfw/yuri/gif](https://purrbot.site/api/img/nsfw/yuri/gif) { #img-nsfw-yuri-gif }
Returns a random Yuri (Lesbian) sex Gif.

=== "Response"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    ```js title="JSON Body Example"
    {
      "error": false,
      "link": "https://purrbot.site/img/nsfw/yuri/gif/yuri_001.gif",
      "time": 0
    }
    ```

=== "Failure"
    **Type:** :octicons-file-code-24: `JSON`  
    **Example:**  
    Please see the [Possible Errors](#possible-errors) section for all errors this API may return.

----

## Possible Errors
Whenever a request fails, either by an error on the client's end or caused by the API itself, will you receive a JSON Body with information regarding the error.

To get more information about a value, click the :material-numeric-1-circle: **Number Icon** next to the value to get a text box with useful information such as type and default value.

### /api/quote { #error-api-quote }

=== "Empty JSON Body/No JSON"
    **Status-Code**: [400]
    
    ```js title="JSON Body Example"
    {
      "details": {
        "path": "/api/quote", // (1)
        "content-type": ":content-type", // (2)
        "user-agent": ":user-agent" // (3)
      },
      "error": true,
      "message": "Received invalid or empty JSON Body."
    }
    ```
    
    1.  The Path you accessed. This should be `/api/quote` for this endoint.
    2.  The content-tyoe you provided. This **must** be `application/json`.
    3.  The User-Agent you used.

=== "Malformed JSON/Invalid Values"
    **Status-Code**: [500]
    
    ```js title="JSON Body Example"
    {
      "details": {
        "path": "/api/quote", // (1)
        "content-type": ":content-type", // (2)
        "user-agent": ":user-agent" // (3)
      },
      "error": true,
      "message": "Couldn't generate Image. Make sure the values are valid!"
    }
    ```
    
    1.  The Path you accessed. This should be `/api/quote` for this endoint.
    2.  The content-tyoe you provided. This **must** be `application/json`.
    3.  The User-Agent you used.

### /api/status { #error-api-status }

=== "Empty JSON Body/No JSON"
    **Status-Code**: [400]
    
    ```js title="JSON Body Example"
    {
      "details": {
        "path": "/api/status", // (1)
        "content-type": ":content-type", // (2)
        "user-agent": ":user-agent" // (3)
      },
      "error": true,
      "message": "Received invalid or empty JSON Body."
    }
    ```
    
    1.  The Path you accessed. This should be `/api/quote` for this endoint.
    2.  The content-tyoe you provided. This **must** be `application/json`.
    3.  The User-Agent you used.

=== "Malformed JSON/Invalid Values"
    **Status-Code**: [500]
    
    ```js title="JSON Body Example"
    {
      "details": {
        "path": "/api/status", // (1)
        "content-type": ":content-type", // (2)
        "user-agent": ":user-agent" // (3)
      },
      "error": true,
      "message": "Couldn't generate Image. Make sure the values are valid!"
    }
    ```
    
    1.  The Path you accessed. This should be `/api/quote` for this endoint.
    2.  The content-tyoe you provided. This **must** be `application/json`.
    3.  The User-Agent you used.

### /api/img/* { #error-api-img }

=== "Invalid Path (No API endpoint)"
    **Status-Code**: [403]
    
    ```js title="JSON Body Example"
    {
      "details": {
        "path": "/api/img/:path", // (1)
        "content-type": ":content-type", // (2)
        "user-agent": ":user-agent" // (3)
      },
      "error": true,
      "message": "The selected API path is not supported!"
    }
    ```
    
    1.  The Path you accessed. Example: `/api/img/sfw/background/img`
    2.  The content-tyoe you provided. This **must** be `application/json`.
    3.  The User-Agent you used.

=== "No Images available"
    **Status-Code**: [404]
    
    ```js title="JSON Body Example"
    {
      "details": {
        "path": "/api/img/:path", // (1)
        "content-type": ":content-type", // (2)
        "user-agent": ":user-agent" // (3)
      },
      "error": true,
      "message": "The selected API path does not contain any images!"
    }
    ```
    
    1.  The Path you accessed. Example: `/api/img/sfw/background/img`
    2.  The content-tyoe you provided. This **must** be `application/json`.
    3.  The User-Agent you used.

[400]: https://httpstatuses.com/400
[403]: https://httpstatuses.com/403
[404]: https://httpstatuses.com/404
[500]: https://httpstatuses.com/500
