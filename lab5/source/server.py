#!/usr/bin/env python3
from flask import Flask, jsonify
import re
from flask import request
import json

#zapoznanie sie z trescia zadania
def calculate(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return {"sum": num1 + num2, "sub": num1 - num2, "mul": num1 * num2, "div": num1 // num2, "mod": num1 % num2}

def statistics(string):
    lowercase = len(re.findall(r'[a-z]', string))
    uppercase = len(re.findall(r'[A-Z]', string))
    digits = len(re.findall(r'[1-9]', string))
    special = len(string) - lowercase - uppercase - digits
    return {
        "lowercase": lowercase,
        "uppercase": uppercase,
        "digits": digits,
        "special": special
    }

app = Flask(__name__)


@app.route("/", methods=['POST'])
def get_numbers():
    request_json = request.get_json()
    string = request_json.get("str")
    num1 = request_json.get("num1")
    num2 = request_json.get("num2")
    return calculate(request.args.get('num1'), request.args.get('num2'))


# --- main ---
if __name__ == '__main__':
    PORT = 4080

    print(f'Starting: http://localhost:{PORT}')
    app.run(debug=False, host='0.0.0.0', port=PORT)
