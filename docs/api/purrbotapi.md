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
	- All provided values need to be String.
	- Leave away a field and value to use the default option.

### Fields
| Field      | Description                                                                                                         | Default                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| avatar     | The URL of the avatar to display.                                                                                   | https://i.imgur.com/36aniDJ.png |
| dateFormat | The format in which the date should be displayed. This uses the [SimpleDateFormat]                                  | `dd. MMM yyyy hh:mm:ss`         |
| message    | The message itself to display. This __won't__ format markdown, emotes and only formats selected emojis.             | `Some message`                  |
| nameColor  | The color, in which the name should be displayed. You can provide `hex:rrggbb`, `rgb:r,g,b` or the raw color value. | `hex:ffffff`                    |
| timestamp  | The date and time as epoch milliseconds.                                                                            | `<Current time of the request>` |
| username   | The name to display.                                                                                                | `Someone`                       |

!!! example
    === "Request"
        <br>
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
	- All provided values need to be String.
	- Leave away a field and value to use the default option.

### Fields
| Field      | Description                                                                                  | Default                         |
| ---------- | -------------------------------------------------------------------------------------------- | ------------------------------- |
| avatar     | The URL of the avatar to display.                                                            | https://i.imgur.com/36aniDJ.png |
| status     | The status to set as icon. Can be `online`, `idle`, `do_not_disturb` (or `dnd`) or `offline` | `offline`                       |

!!! example
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

!!! example "Error responses"
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