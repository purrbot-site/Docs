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
    
    --8<-- "api-error-scheme.md"
    
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
    
    --8<-- "api-error-scheme.md"
