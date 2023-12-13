from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/remove_task/<int:index>')
def remove_task(index):
    if index >= 0 and index < len(tasks):
        removed_task = tasks.pop(index)
        return f"Tarefa '{removed_task}' removida da lista."
    else:
        return "Índice inválido."

if __name__ == '__main__':
    app.run(debug=True)
