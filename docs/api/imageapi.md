[SimpleDateFormat]: https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html

# ImageAPI
The ImageAPI was created to be a replacement for the nekos.life API in the bot \*Purr\*.  
It is publicly available to use.

!!! warning "Important"
    - All requests are performed through GET requests
    - No JSON body or similiar is required for the API.

## SFW (Safe for work) endpoints
Contains images that are considered safe for work.

!!! note "Base-URL"
    https://purrbot.site/api/img/sfw

### /background/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/background/img/gradient_orange.png",
  "time": 0
}
```

### /bite/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purbot.site/img/sfw/bite/gif/bite_001.gif",
  "time": 0
}
```

### /cuddle/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/cuddle/gif/cuddle_001.gif",
  "time": 0
}
```

### /feed/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/feed/gif/feed_001.gif",
  "time": 0
}
```

### /holo/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/holo/img/holo_001.jpg",
  "time": 0
}
```

### /hug/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/hug/gif/hug_001.gif",
  "time": 0
}
```

### /icon/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/icon/img/purr.png",
  "time": 0
}
```

### /kiss/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/kiss/gif/kiss_001.gif",
  "time": 0
}
```

### /kitsune/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/kitsune/img/kitsune_001.jpg",
  "time": 0
}
```

### /lick/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/lick/gif/lick_001.gif",
  "time": 0
}
```

### /neko/:type
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

### /pat/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/pat/gif/pat_001.gif",
  "time": 0
}
```

### /poke/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/poke/gif/poke_001.gif",
  "time": 0
}
```

### /senko/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/senko/img/senko_001.jpg",
  "time": 0
}
```

### /slap/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/slap/gif/slap_001.gif",
  "time": 0
}
```

### /tail/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/tail/gif/tail_001.gif",
  "time": 0
}
```

### /tickle/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/tickle/gif/tickle_001.gif",
  "time": 0
}
```

----

## NSFW (Not safe for work) endpoints
Contains images that are considered Not Safe for work.  
If you are using those images on Discord, make sure to only share them in Channels marked as NSFW.

!!! note "Base-URL"
    https://purrbot.site/api/img/nsfw

### /anal/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/anal/gif/anal_001.gif",
  "time": 0
}
```

### /blowjob/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/blowjob/gif/blowjob_001.gif",
  "time": 0
}
```

### /fuck/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/fuck/gif/fuck_001.gif",
  "time": 0
}
```

### /neko/:type
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

### /pussylick/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/pussylick/gif/pussylick_001.gif",
  "time": 0
}
```

### /solo/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/solo/gif/solo_001.gif",
  "time": 0
}
```

### /threesome_fff/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/threesome_fff/gif/threesome_001.gif",
  "time": 0
}
```

### /threesome_ffm/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/threesome_ffm/gif/threesome_001.gif",
  "time": 0
}
```

### /threesome_mmf/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/threesome_mmf/gif/threesome_001.gif",
  "time": 0
}
```

### /yuri/gif
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

=== "Not existing path"
    When you connect to an API path which does not exist (e.g. `/api/img/doesntexist`) will this error response be displayed.
    
    ```json
    {
      "code": 403,
      "message": "Not supported API path",
      "time": 0
    }
    ```
    
=== "Path doesn't contain any images"
    If the provided path doesn't contain any images, will this error be displayed.
    
    ```json
    {
      "code": 403,
      "message": "The selected directory doesn't contain any images",
      "time": 0
    }
    ```
