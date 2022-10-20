#!/usr/bin/env python3
import http.server
import socketserver
import os

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        
        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()   
            msgToBePrinted = "Hello World!"         
            if rev:
            	msgToBePrinted = rev(txt)	           	
            msgToBePrinted = msgToBePrinted + "\n"
            self.wfile.write(msgToBePrinted.encode(encoding = 'UTF-8'))
 	elif self.path.startswith('/cmd'):
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()   
            if self.path.split('=')[1] == 'time':
            	msgToBePrinted = datetime.now().strftime("%H:%M:%S")
            elif self.path.split('=')[1] == 'rev&str':
            	msgToBePrinted = rev(self.path.split('=')[2])
            msgToBePrinted = msgToBePrinted + "\n"
            self.wfile.write(msgToBePrinted.encode(encoding = 'UTF-8'))
        else:
            super().do_GET()
            
     def rev(x):
  	return x[::-1]
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
