## Cross Site Request Forgery
#### February 29, 2016

Cross Site Request Forgery or CSRF or XSRF is a malicious exploit of a website where unauthorized codes are transmitted from the user it trusts. 

Methods to prevent CSRF:

* Synchronizer token pattern: An unique and secret token is embedded with form data in each request to the server.

* Cookie-to-Header token: on login, cookie is set up with random token value. When js code seems a request, it reads the token from cookie and sends it in request header. The server validates the token.

--
