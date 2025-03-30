# Simple HTTP Server 


## Browser  

Open a Browser and enter the following URL: `http://localhost:8080/hello.html`

## curl 

```bash
$ curl -v http://localhost:8080/hello.html
*   Trying 127.0.0.1:8080...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> GET /hello.html HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 252
< Connection: close
< 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple HTTP Server</title>
</head>
<body>
    <h1>Hello, welcome to my HTTP server!</h1>
    <p>This is a simple HTML page served by a basic HTTP server.</p>
</body>
</html>
* Closing connection 0
```
