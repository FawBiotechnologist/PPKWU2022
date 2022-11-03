#!/usr/bin/env python3
import http.server
import socketserver
import json
import re
from urllib.parse import unquote


def statistics(string):
    lowercase = len(re.findall(r'[a-z]', string))
    uppercase = len(re.findall(r'[A-Z]', string))
    digits = len(re.findall(r'[1-9]', string))
    special = len(string) - lowercase - uppercase - digits
    return json.dumps({
        "lowercase": lowercase,
        "uppercase": uppercase,
        "digits": digits,
        "special": special
    })


class web_server(http.server.SimpleHTTPRequestHandler):
    def set_header(self, string):
        self.protocol_version = 'HTTP/1.1'
        self.send_response(200)
        self.send_header("Content-type", string)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self.set_header('text/html; charset = UTF-8')
            msgToBePrinted = "Undefined Behaviour"
            self.wfile.write(msgToBePrinted.encode(encoding='UTF-8'))
        elif self.path.startswith('/str='):
            try:
                self.set_header("application/json")
                to_be_parsed = self.path.split('=')[1]
                to_be_parsed = unquote(to_be_parsed)
                self.wfile.write(bytes(statistics(to_be_parsed),encoding='UTF-8'))
            except Exception:
                self.wfile.write(bytes('Some exception occurred',encoding='UTF-8'))
        else:
            super().do_GET()


# --- main ---
PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("", PORT), web_server)
tcp_server.serve_forever()

