#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
    result = ''
    for num in range(int(parameter)):
        result += f'{num}\n'
    return result
@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)
    operations = {
        '+': num1 + num2, '-': num1 - num2, '*': num1 * num2, 'div': num1/num2, '%': num1%num2
    }
    if operation in operations:
        result = operations[operation]
    else:
        result = 'Error'

    return str(result)
    