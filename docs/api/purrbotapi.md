[SimpleDateFormat]: https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html
[link]: https://i.imgur.com/36aniDJ.png
[base-url]: https://purrbot.site/api

# PurrBotAPI
API used to create dynamic images based on the provided input.

!!! note "Base-URL"
    [https://purrbot.site/api][base-url]

!!! tip "Important"
    - All requests are performed through POST requests
	- The request body needs to contain valid JSON. Even when it is empty.

## /quote
*Generates images that look like Discord messages*

!!! note "Info"
    - Returns an image on success and JSON on failure.
	- All provided values need to be String.
	- Leave away a field and value to use the default option.

### Fields
| Field      | Description                                                                                                         | Default                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| avatar     | The URL of the avatar to display.                                                                                   | [https://i.imgur.com/36aniDJ.png][link] |
| dateFormat | The format in which the date should be displayed. This uses the [SimpleDateFormat]                                  | `dd. MMM yyyy hh:mm:ss`                 |
| message    | The message itself to display. This __won't__ format markdown, emotes and only formats selected emojis.             | `Some message`                          |
| nameColor  | The color, in which the name should be displayed. You can provide `hex:rrggbb`, `rgb:r,g,b` or the raw color value. | `hex:ffffff`                            |
| timestamp  | The date and time as epoch milliseconds.                                                                            | `<The current time of the request>`     |
| username   | The name to display.                                                                                                | `Someone`                               |

!!! example "Example JSON-request"
    ```json  
    {  
      "avatar": "https://cdn.discordapp.com/avatars/204232208049766400/ae7f2e5247a05791dbf0ef96243622c2.png",  
      "message": "This is an example message.",  
      "nameColor": "hex:ff0000"  
      "username": "Andre_601"  
    }  
    ```

## /status
*Adds a status icon to the provided avatar*

!!! note "Info"
    - Returns an image on success and JSON on failure.
	- All provided values need to be String.
	- Leave away a field and value to use the default option.

### Fields
| Field      | Description                                                                                  | Default                                 |
| ---------- | -------------------------------------------------------------------------------------------- | --------------------------------------- |
| avatar     | The URL of the avatar to display.                                                            | [https://i.imgur.com/36aniDJ.png][link] |
| status     | The status to set as icon. Can be `online`, `idle`, `do_not_disturb` (or `dnd`) or `offline` | `offline`                               |

## Error responses
The API might return certain errors, depending on different facors.  
Possible errors are a `500 Internal server error` or a `403 Unauthorized error`.

Both are returned as JSON looking something like this:  
```json
{
  "code": 403,
  "message": "Invalid or empty JSON-body received!"
}
```