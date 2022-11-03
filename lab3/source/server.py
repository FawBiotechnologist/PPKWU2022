#!/usr/bin/env python3
import http.server
import socketserver
import json
import re


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
        else:
            super().do_GET()


# --- main ---
PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("", PORT), web_server)
tcp_server.serve_forever()

