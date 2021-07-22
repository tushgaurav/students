from cs50 import SQL
from flask import Flask, render_template, request

db = SQL("sqlite:///students.db")


app = Flask(__name__)

BRANCHES = [
    "CSE",
    "ECE",
    "CSE DS",
    "CSE AI",
    "CSE ML",
    "CSE IT",
    "CS",
    "Mechanical",
    "Civil",
    "Chemical",
    "Bio Tech"
    ]


@app.route("/")
def index():
    return render_template("index.html", branches=BRANCHES)


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":

        name = request.form.get('name')
        roll = int(request.form.get('roll'))
        number = request.form.get('number')
        email = request.form.get('email')
        address = request.form.get('address')
        stream = request.form.get('stream')

        db.execute("INSERT INTO students (name, number, email, address, stream, id) VALUES (?, ?, ?, ?, ?, ?)", name, number, email, address, stream, roll)
        return "Success!"

