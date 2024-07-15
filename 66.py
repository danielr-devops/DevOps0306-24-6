from flask import Flask, request

app = Flask("moshe")


@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/cars', methods=['GET', 'POST'])
def cars():
    if request.method == "GET":
        return "Mazda, Chevrolet, Citroen, Hyundai"
    elif request.method == "POST":
        return "Creating new car", 201


@app.route('/motors', methods=['GET', 'POST'])
def motors():
    if request.method == "GET":
        return "Honda, Yamaha"
    elif request.method == "POST":
        return "Creating new Motorbike", 201


app.run(debug=True)
