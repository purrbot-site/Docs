[SimpleDateFormat]: https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html

# PurrBotAPI
API used to create dynamic images based on the provided input.

!!! note "Base-URL"
    https://purrbot.site/api

!!! warning "Important"
    - All requests are performed through POST requests
    - The request body needs to contain valid JSON. Even when it is empty.

## /quote
*Generates images that look like Discord messages*

!!! note "Info"
    - Returns an image on success and JSON on failure.
    - Leave away a field and value to use the default option.

### Fields

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

### Example

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

## /status
*Adds a status icon to the provided avatar*

!!! note "Info"
    - Returns an image on success and JSON on failure.
    - Leave away a field and value to use the default option.

### Fields

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
    

### Example

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

## Error responses
The API might return certain errors, depending on different facors.  
Possible errors are a `500 Internal Server Error` or a `403 Unauthorized Error`.

=== "500 Internal Server Error"
    If you receive the below error response will you need to check, if the values you provided are valid.  
    A possible issue could be a image-link being invalid.
    
    ```json
    {
      "code": 500,
      "message": "Couldn't generate image. Make sure the values are valid!"
    }
    ```
    
=== "403 Unauthorized Error"
    If you receive the below error response, does it mean that your provided JSON body was malformed (invalid).  
    This means, that you forgot to format it properly (i.e. forgot a comma) or you didn't provide any JSON at all.
    
    ```json
    {
      "code": 403,
      "message": "Invalid or empty JSON-body received!"
    }
    ```
