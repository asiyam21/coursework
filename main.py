from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy, model

app = Flask(__name__)

app.congif['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Destination(db.model):
    timeOfYear = db.column(db.String(8), primary_key=True, nullable = False)
    holidayType = db.column(db.String(20),primary_key=True, nullable = False)
    weather = db.column(db.String(8), nullable = False)
    activities = db.column(db.String(10), nullable = False)
    price = db.column(db.Integer, primary_key=True, nullable = False)

class flights(db.model):
    timeOfYear = db.relationship('Destination', backref = 'author', lazy = True)
    price = db.relationship('destination', backref = 'author', lazy = True)
    airport = db.column(db.String(20), nullable = False)
    time = db.column(db.Integer, nullable = False)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/questionnaire")
def questionnaire():
    return render_template("questionnaire.html")

@app.route("/results")
def results():
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True)
