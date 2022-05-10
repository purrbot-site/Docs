??? failure "403"
    **Type:** :octicons-file-code-24: `application/json`
    
    ```json title="Example"
    {
      "details": {
        "path": "/api/img/:path",
        "content-type": ":your-content-type",
        "user-agent": ":your-user-agent"
      },
      "error": true,
      "message": "The provided path is not valid.",
      "time": 0
    }
    ```
    
    <h4>Schema</h4>
    
    - `details`: JSON Object  
      Contains details about your request.
        - `path`: String  
          The path you accessed. Always starts with `/api/img/`.
        - `content-type`: String  
          The content-type you provided in your request.
        - `user-agent`: String  
          The User-Agent you used in your request.
    - `error`: Boolean  
      Always returns true for errors.
    - `message`: String  
      The reason why the request failed.
    - `time`: Integer  
      Time in milliseconds it took for the API to process the request.
    
??? failure "404"
    **Type:** :octicons-file-code-24: `application/json`
    
    ```json title="Example"
    {
      "details": {
        "path": "/api/img/:path",
        "content-type": ":your-content-type",
        "user-agent": ":your-user-agent"
      },
      "error": true,
      "message": "The provided path does not contain any images.",
      "time": 0
    }
    ```
    
    <h4>Schema</h4>
    
    - `details`: JSON Object  
      Contains details about your request.
        - `path`: String  
          The path you accessed. Always starts with `/api/img/`.
        - `content-type`: String  
          The content-type you provided in your request.
        - `user-agent`: String  
          The User-Agent you used in your request.
    - `error`: Boolean  
      Always returns true for errors.
    - `message`: String  
      The reason why the request failed.
    - `time`: Integer  
      Time in milliseconds it took for the API to process the request.
