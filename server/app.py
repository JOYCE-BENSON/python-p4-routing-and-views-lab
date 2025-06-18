#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Index view with base URL"""
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    """Print string view that prints to console and displays in browser"""
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    """Count view that displays numbers in range on separate lines"""
    numbers = []
    for i in range(parameter):
        numbers.append(str(i))
    return '\n'.join(numbers) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    """Math view that performs operations on two numbers"""
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)