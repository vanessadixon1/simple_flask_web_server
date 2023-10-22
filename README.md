# Simple Flask Web Server

This is a simple Flask Web Server that listens for http request and responds.

### Features

   ### Greet
   * user is able to send a http get request using a http client(postman, insonmia, browser, etc) for data from the following web api endpoints:
       * /welcome - return "weclome"
       * /welcome/home retrun "welcome home"
       * /welcome/back return "welcome back"
       * 
   ## calc
   * user is able to send a http get request using a http client(postman, insonmia, browser, etc)  with 2 param args to perform a math operation on the numbers to the following web api endpoints:
      * /add
      * /sub
      * /mult
      * /div
      * /math/<operation>

### Technologies used:
* Python
* Flask
