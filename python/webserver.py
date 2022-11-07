from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime as dt

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        mydt = dt.datetime.now()
        message = "Date: " + mydt.strftime("%Y-%m-%d")
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()