#!/usr/bin/env python3
from flask import Flask, Response
import re
from flask import request
import xmltodict
from dict2xml import dict2xml


def calculate(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return {"sum": num1 + num2, "sub": num1 - num2, "mul": num1 * num2, "div": num1 // num2, "mod": num1 % num2}


def statistics(string):
    lowercase = len(re.findall(r'[a-z]', string))
    uppercase = len(re.findall(r'[A-Z]', string))
    digits = len(re.findall(r'[0-9]', string))
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
    request_xml = request.get_data()
    content = xmltodict.parse(request_xml)
    string = content.get("str")
    if string is None:
        content = content.get("root")
        string = content.get("str")
    stringDictionary = {}
    numberDictionary = {}
    if string is not None:
        stringDictionary = statistics(string)
    num1 = content.get("num1")
    num2 = content.get("num2")
    if num1 is not None and num2 is not None:
        numberDictionary = calculate(num1, num2)
    stringDictionary.update(numberDictionary)
    xml = dict2xml(stringDictionary, wrap='root')
    return Response(xml, mimetype='text/xml')


if __name__ == '__main__':
    PORT = 4080

    print(f'Starting: http://localhost:{PORT}')
    app.run(debug=False, host='0.0.0.0', port=PORT)
