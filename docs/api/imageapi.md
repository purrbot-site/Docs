[SimpleDateFormat]: https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html

# ImageAPI
The ImageAPI was created to be a replacement for the nekos.life API in the bot \*Purr\*.  
It is publicly available to use.

!!! tip "Important"
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
  "link": "https://purrbot.site/img/sfw/background/img/gradient_orange.png"
}
```

### /cuddle/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/cuddle/gif/cuddle_001.gif"
}
```

### /holo/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/holo/img/holo_001.jpg"
}
```

### /hug/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/hug/gif/hug_001.gif"
}
```

### /icon/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/icon/img/purr.png"
}
```

### /kiss/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/kiss/gif/kiss_001.gif"
}
```

### /kitsune/img
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/kitsune/img/kitsune_001.jpg"
}
```

### /lick/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/lick/gif/lick_001.gif"
}
```

### /neko/:type
`:type` can be either `gif` for gifs or `img` for images.

Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/neko/img/neko_001.jpg"
}
```

### /pat/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/pat/gif/pat_001.gif"
}
```

### /poke/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/poke/gif/poke_001.gif"
}
```

### /slap/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/slap/gif/slap_001.gif"
}
```

### /tickle/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/sfw/tickle/gif/tickle_001.gif"
}
```

----

## NSFW (Not safe for work) endpoints
Contains images that are considered Not Safe for work.

!!! note "Base-URL"
    https://purrbot.site/api/img/nsfw

### /blowjob/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/blowjob/gif/blowjob_001.gif"
}
```

### /fuck/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/fuck/gif/fuck_001.gif"
}
```

### /neko/:type
`:type` can be either `gif` for gifs or `img` for images.

Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/neko/img/neko_001"
}
```

### /solo/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/solo/gif/solo_001.gif"
}
```

### /threesome_fff/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/threesome_fff/gif/threesome_001.gif"
}
```

### /threesome_ffm/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/threesome_ffm/gif/threesome_001.gif"
}
```

### /threesome_mmf/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/threesome_mmf/gif/threesome_001.gif"
}
```

### /yuri/gif
Example response:  
```json
{
  "code": 200,
  "link": "https://purrbot.site/img/nsfw/yuri/gif/yuri_001.gif"
}
```

----

## Failed requests
The API can return one of two error responses, depending on which one is the case.

### Not existing path
Send when an illegal/not supported path was provided.

Example response:  
```json
{
  "code": 403,
  "message": "Not supported API path."
}
```

### Folder doesn't contain any images
Send when a provided path leads to a directory without any images.

Example response:  
```json
{
  "code": 403,
  "message": "The selected directory doesn't contain any images."
}
```