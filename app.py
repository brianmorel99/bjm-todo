from flask import Flask, render_template, request, url_for, redirect
from todo import Todo

app = Flask(__name__)

todo = Todo()
todo.name = 'test'
todo.desc = 'Test Todo'
todo.complete = True
todos = [todo]

@app.route("/")
def index():
    return render_template('index.html', todos=todos)

@app.route("/add", methods=["POST"])
def add():
    todo = Todo()
    todo.name = request.form['name']
    todo.desc = request.form['desc']
    todo.complete = False
    todos.append(todo)
    return redirect(url_for('index'))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todos[index].name = request.form['name']
        todos[index].desc = request.form['desc']
        todos[index].complete = request.form.get('complete') != None
        return redirect(url_for('index'))
    else:
        return render_template("edit.html", todo = todo, index = index)

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)