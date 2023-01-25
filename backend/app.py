from flask import Flask, json, request
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="tasksDB"
)


def create_cursor():
    cnx = mydb.cursor()

    return cnx


insert_task = ("INSERT INTO tasks "
               "(titolo, contenuto, `data`, stato) "
               "VALUES (%s, %s, %s, %s)")


def add_task():
    cnx = create_cursor()
    task_data = (request.json['titolo'], request.json['contenuto'], request.json['data'], request.json['stato'])
    cnx.execute(insert_task, task_data)
    mydb.commit()
    cnx.close()


def get_tasks():
    cnx = create_cursor()
    cnx.execute("SELECT * FROM tasks")
    tasks = cnx.fetchall()
    cnx.close()
    return tasks


@app.route("/")
def hello_world():
    return "<p>WELCOME</p>"


@app.route("/tasks", methods=["GET", "POST"])
def view_tasks():
    if request.method == "GET":
        tasks = get_tasks()
        return json.dumps(tasks), 200, {'ContentType': 'application/json'}
    elif request.method == "POST":
        add_task()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    cnx = create_cursor()
    cnx.execute("DELETE FROM tasks WHERE id = %s", (id,))
    mydb.commit()
    cnx.close()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/tasks/<int:id>", methods=["PUT"])
def task_done(id):
    cnx = create_cursor()
    cnx.execute("UPDATE tasks SET stato = NOT stato WHERE id = %s", (id,))
    mydb.commit()
    cnx.close()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
