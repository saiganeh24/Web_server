
from http.server import HTTPServer,BaseHTTPRequestHandler

content="""
<html>
<head>
<body>
<h1>Welcome To My Web page</h1>
</head>
</body>
</hmtl>
"""

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
