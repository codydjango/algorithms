# HTTP Evolution

## HTTP
* unique TCP connection for every request

## HTTP/1.0
* introduced headers
* default behaviour is to open a separate TCP connection for each request/response pair.

## HTTP/1.1
* can reuse TCP connection for multiple resources (pipelining and persistant connections, can be partially controlled using the connection header)

## HTTP/2
* multiplexing messages over single connection keeping connection active and more efficient.
* introduced frames, providing optimization and performance improvements.
* encapsulation in frames means they are impossible to read directly.
* pipelining has been superseded in in http/2 by multiplexing requests within a frame
* a frame is a binary representation of part of the http message, allowing for compression and multiplexing. the client reconstitutes to the original http/1.1, so it's still very useful to understand the 1.1 semantics.


