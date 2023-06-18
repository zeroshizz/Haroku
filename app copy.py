from flask import Flask, render_template, request, abort

app = Flask(__name__)

stacks = {}

@app.route('/calc/<int:id>/peek', methods=['GET', 'POST'])
def peek(id):
    if id not in stacks:
        abort(404, description="Stack not found.")
    if len(stacks[id]) == 0:
        return "Stack is empty."
    return str(stacks[id][-1])

@app.route('/calc/<int:id>/push/<int:n>', methods=['GET', 'POST'])
def push(id, n):
    if id not in stacks:
        stacks[id] = []
    stacks[id].append(n)
    return "Pushed {} to stack {}.".format(n, id)

@app.route('/calc/<int:id>/pop', methods=['GET', 'POST'])
def pop(id):
    if id not in stacks:
        abort(404, description="Stack not found.")
    if len(stacks[id]) == 0:
        return "Stack is empty."
    return str(stacks[id].pop())

@app.route('/calc/<int:id>/add', methods=['GET', 'POST'])
def add(id):
    if id not in stacks:
        abort(404, description="Stack not found.")
    if len(stacks[id]) < 2:
        return "Stack does not have enough numbers to add."
    a = stacks[id].pop()
    b = stacks[id].pop()
    stacks[id].append(a + b)
    return "Added {} and {} and pushed the result to stack {}.".format(a, b, id)

@app.route('/calc/<int:id>/subtract', methods=['GET', 'POST'])
def subtract(id):
    if id not in stacks:
        abort(404, description="Stack not found.")
    if len(stacks[id]) < 2:
        return "Stack does not have enough numbers to subtract."
    a = stacks[id].pop()
    b = stacks[id].pop()
    stacks[id].append(b - a)
    return "Subtracted {} from {} and pushed the result to stack {}.".format(a, b, id)

@app.route('/calc/<int:id>/multiply', methods=['GET', 'POST'])
def multiply(id):
    if id not in stacks:
        abort(404, description="Stack not found.")
    if len(stacks[id]) < 2:
        return "Stack does not have enough numbers to multiply."
    a = stacks[id].pop()
    b = stacks[id].pop()
    stacks[id].append(a * b)
    return "Multiplied {} and {} and pushed the result to stack {}.".format(a, b, id)

@app.route('/calc/<int:id>/divide', methods=['GET', 'POST'])
def divide(id):
    if id not in stacks:
        abort(404, description="Stack not found.")
    if len(stacks[id]) < 2:
        return "Stack does not have enough numbers to divide"
    a = stacks[id].pop()
    b = stacks[id].pop()
    if a == 0:
        return "Cannot divide by zero."
    stacks[id].append(b / a)
    return "Divided {} by {} and pushed the result to stack {}.".format(b, a, id)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)