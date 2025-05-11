# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample GET endpoint
@app.route('/greet', methods=['GET'])
def greet():
    # Query Parameters Should be used in the GET request
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

# Sample POST endpoint
@app.route('/add', methods=['POST'])
def add_numbers():
    # Will accept only POST request, We can't GET it from Browser
    # get_json() should be used for POST requests
    data = request.get_json()
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    result = num1 + num2
    return jsonify({"result": result})

@app.route('/multiply', methods=['GET','POST'])
def multiply_nums():
    # can accept both GET, POST Request
    # http://127.0.0.1:5000/multiply?num1=5&num2=7
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({'result': data['num1'] * data['num2']})
    else:  # GET
        num1 = int(request.args.get('num1', 0))
        num2 = int(request.args.get('num2', 0))
        return jsonify({'result': num1 * num2})


if __name__ == '__main__':
    app.run(debug=True)
