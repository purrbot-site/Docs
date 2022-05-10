<h4>Schema</h4>

- `details`: JSON Object  
  Contains details about your request.
    - `path`: String  
      The path you accessed.
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