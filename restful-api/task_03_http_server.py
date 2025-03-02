#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

"""
import http.server module
"""


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            json_response = {"name": "John", "age": 30, "city": "New York"}
            response = json.dumps(json_response)
            self.wfile.write(response.encode(encoding='utf_8'))
        elif self.path == "/status":
            self.send_response(200)
            self.end_headers()
            self.wfile.write("OK".encode(encoding='utf_8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("URL not found".encode(encoding='utf_8'))


def run(server_class=HTTPServer, handler_class=Server):
    """
    function of the server
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server listening in port 8000")
    httpd.serve_forever()

run()
