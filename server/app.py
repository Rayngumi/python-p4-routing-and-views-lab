#!/usr/bin/env python3

from flask import Flask
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>', 200


@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter, file=sys.stdout) 
    return f'{parameter}', 200

@app.route('/count/<int:parameter>')
def count_route(parameter):
    count_result = "\n".join(str(i) for i in range(parameter)) + "\n"
    return count_result, 200

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_route(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    else:
        return '0', 400
    return str(result), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)