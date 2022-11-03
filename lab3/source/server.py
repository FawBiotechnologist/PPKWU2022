#!/usr/bin/env python3
import http.server
import socketserver
import os
import json


# print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):

        print(self.path)

        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            msgToBePrinted = "Undefined Behaviour"
            self.wfile.write(msgToBePrinted.encode(encoding='UTF-8'))
        elif self.path.startswith('/str='):
            to_be_parsed = self.path.split('=')[1]
            print(to_be_parsed)
        else:
            super().do_GET()
# { "lowercase" : liczba, "uppercase" : liczba, "digits" : liczba, "special" : liczba}

# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("", PORT), web_server)
tcp_server.serve_forever()

