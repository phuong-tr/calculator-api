from flask import Flask, request, jsonify
from app import calc

app = Flask(__name__)

@app.route('/calc', methods=['POST'])
def calculate():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    op = data.get('operation')

    if op == 'add':
        result = calc.add(a, b)
    elif op == 'subtract':
        result = calc.subtract(a, b)
    elif op == 'multiply':
        result = calc.multiply(a, b)
    elif op == 'divide':
        result = calc.divide(a, b)
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
