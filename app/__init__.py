from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the Flask Testing API'


@app.route('/add', methods=['POST'])
def add_values():
    if not request.is_json:
        return {'error': 'Content-Type must be application/json'}, 400
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return {'error': 'Bad data, values must be int or float'}, 400
    return {'result': num1+num2}


@app.route('/subtract', methods=['POST'])
def subtract_values():
    if not request.is_json:
        return {'error': 'Content-Type must be application/json'}, 400
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return {'error': 'Bad data, values must be int or float'}, 400
    return {'result': num1 - num2}
