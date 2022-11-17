#!/usr/bin/env python3
from flask import Flask
import re
from flask import request
import json


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
    
app = Flask(__name__)
# print('source code for "http.server":', http.server.__file__)
@app.route("/",methods=['GET'])
def stats():
	return statistics(request.args.get('str'))
	

# --- main ---
if __name__ == '__main__':
	
	PORT = 4080

	print(f'Starting: http://localhost:{PORT}')
	app.run(debug=False,host='0.0.0.0',port = PORT)

