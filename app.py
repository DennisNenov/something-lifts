from flask import Flask,render_template, session, redirect, request, url_for
from pymongo import Connection
conn = Connection()
db = conn['a']
app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("index.html")

@app.route("/macros")
def macros():
    return render_template("macros.html")

@app.route("/workout")
def workout():
    return render_template("workout.html")

@app.route("/graphs")
def graphs():
    weightlist = db.users.find_one({"username": username})["weightlist"]
    gains = db.users.find_one({"username": username})["gains"] #tracks progress in weights, change name if you want to make it more clear; gains will be a dictionary, for example: {squat: [50, 60, 70], deadlift: [100, 200, 300]}
    return render_template("graphs.html", weightlist=weightlist, gains=gains)

@app.route("/goals")
def goals():
    if request.method == "POST":
        weight = request.form.get("weight", None)
        goal = request.form.get("goal", None)
        if goal == "lose weight":
            return render_template("loseweight.html", weight=weight)
        if goal == "hypertrophy":
            return render_template("hypertrophy.html", weight=weight)
       #keep copy+pasting and changing the goals to the different goals youre going to include
    return render_template("goals.html")

@app.route("/login")
def login():
    if request.method == "POST":
        username = request.form.get("username", None) #name the element in the html form username; return none if no value is found in username
        password = request.form.get("password", None)
        if db.users.find_one({'name': username, 'password': password}) != None:
            return redirect(url_for('goals'))
    return render_template("login.html", username=username)

@app.route("/signup")
def signup():
    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        db.users.insert({'name': username, 'password': password, 'weight': 0, 'goal': 'None'})
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('username',None)
    return redirect("/")

if __name__=="__main__":
    app.debug=True
    app.run(host = '0.0.0.0')

