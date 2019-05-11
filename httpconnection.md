# HTTP Connection 

## Request

Http request is a "directive" text-based request divided into three blocks. A CRLF (carriage return, line feed) (empty line) separates the head from the body.

Start line and headers are referred to as "head", while the payload below the empty space is referred to as the "body".

1. the request method, followed by path, followed by http protocol version
2. header information giving server information about data requested
3. optional data block for POST data

##### Request Headers:

* User-agent: which browser we're using
* Accept: which mimetypes are acceptable
* Accept-Encoding: which encodings are acceptable
* Accept-Language: which languages are acceptable
* Connection: if we're connecting a keep alive connection for multiple resources
* Host
* Cookie
* Content-Length: if there is a post body, the length of it

## Response

An http response is structured very similarly to an http request. It is formed of text directives, separated by CRLF, and divided into three blocks:

1. Status line which indicates the acknowledgment of HTTP version and status of the request
2. HTTP response headers, giving client information about data sent
3. Final block is optional data block, if the server is returning optional data

##### Response Headers:

* Cache-control: server telling browser how long to cache the data
* Content-type: server telling browser the mimetype of the content and character set encoding
* Content-encoding: server telling browser which encoding was used

##### Sources: 

* https://developer.mozilla.org/en-US/docs/Web/HTTP/Session
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages