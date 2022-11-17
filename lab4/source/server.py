#!/usr/bin/env python3
from flask import Flask
import re
from flask import request
import json



def calculate(num1,num2):
	num1 = int(num1)
	num2 = int(num2)
	return json.dumps(
	 { "sum" : num1+num2, "sub" : num1-num2, "mul" : num1*num2, "div" : num1/num2, "mod" : num1%num2
	 }
	)
app = Flask(__name__)
@app.route("/",methods=['GET'])
def get_numbers():
	return calculate(request.args.get('num1'),request.args.get('num2'))
	

# --- main ---
if __name__ == '__main__':
	
	PORT = 4080

	print(f'Starting: http://localhost:{PORT}')
	app.run(debug=False,host='0.0.0.0',port = PORT)

