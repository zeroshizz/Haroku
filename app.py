from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  # SQLite database file path
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), nullable=False)
    task = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id}>'


# Create the table if it doesn't exist
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    user = request.form['user']
    task = request.form['task']
    new_todo = Todo(user=user, task=task)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
