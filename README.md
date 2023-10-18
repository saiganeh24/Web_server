# Developing a Simple Webserver
NAME:SAI GANESH DEPURU
REF NO:23009248
DEP:AI&ML
=======

# AIM:

Develop a webserver to display about top five web application development frameworks.

# DESIGN STEPS:

## Step 1:

HTML content creation is done

## Step 2:

Design of webserver workflow

## Step 3:

Implementation using Python code

## Step 4:

Serving the HTML pages.

## Step 5:

Testing the webserver
# PROGRAM:
```
from http.server import HTTPServer,BaseHTTPRequestHandler

content="""
<html>
<head>
<body>
<h1>Welcome To My Web page</h1>
</head>
</body>
</hmtl>

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html;charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

print("Welcome To The Sai Ganesh Webpage")
server_address=('',80)
httpd=HTTPServer(server_address,HelloHandler)
httpd.serve_forever()
```
# OUTPUT:
![Alt Text](images/Screenshot%202023-10-05%20094014.png)

# RESULT:

The program is executed succesfully.

