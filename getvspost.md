# GET vs POST

The most common request types:

## GET

GET is for fetching a resource:

`/test/demo_form.php?name1=value1&name2=value2`

* idempotent
* cacheable
* bookmarkable
* no body
* remain in browser history
* limited length (since data is passed via url, and url has a max character count definined by server)
* only ascii characters
* encoding `application/x-www-form-urlencoded`
* data is stored in webserver logs because it's part of the url

## POST

POST is for creating or updating a resource:

`
POST /test/demo_form.php HTTP/1.1
Host: w3schools.com
name1=value1&name2=value2
`

* data contained in body
* aren't cached
* can't be bookmarked
* do not remain in browser history
* no restrictions on data length
* any type of data including binary
* encoding: `application/x-www-form-urlencoded` for text
* encoding: `multipart/form-data` for binary data
* data not stored in webserver logs because data is not part of the url


Source: https://www.w3schools.com/tags/ref_httpmethods.asp
