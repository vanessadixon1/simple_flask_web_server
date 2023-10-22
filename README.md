# Simple Flask Web Server

This is a simple Flask Web Server that listens for http request and response. This web server has greet web api endpoints and it has cal web api endpoint that return some data to the view based on param args and pathvariable

### Features
* Add 5 or less new Memes
###Greet
* user is able to use an http client(postman, insonmia, browser, etc) to send a get request for data from the following web api endpoint:
    * /welcome - return "weclome"
    * /welcome/home retrun "welcome home"
    * /welcome/back return "welcome back"
###calc
* user is able to use an http client(postman, insonmia, browser, etc) to send a get request with 2 param args to perform a math operation on the numbers to the following web api endpoints:
   * /add
   * /sub
   * /mult
   * /div
   * /math/<operation>

### Technologies used:
* Python
* Flask
