from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(add(a,b))

@app.route("/sub")
def sub_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(int(sub(a,b)))

@app.route("/mult")
def multiply_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(int(mult(a,b)))

@app.route("/div")
def div_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(int(div(a,b)))

@app.route("/math/<operation>")
def cal(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])

    operations = {
        "add" : add,
        "sub" : sub,
        "mult" : mult,
        "div" : div,
    }

    return str(int(operations[operation](a,b)))


