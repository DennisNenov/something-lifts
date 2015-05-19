from flask import Flask,render_template, session, redirect, request, url_for, g, flash
from functools import wraps
from pymongo import Connection
import mongo
import tools
import auth

conn = Connection()
db = conn['a']
app = Flask(__name__)

NOT_LOGGED_IN = "You are not logged in!"
ALREADY_LOGGED_IN = "You are already logged in!"

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		not_logged_in = 'user' not in session

		if not_logged_in:
			return redirect(url_for('login', next=request.url))
		return f(*args, **kwargs)
	return decorated_function

@app.route("/") 
def home():
    return render_template("index.html")

@app.route('/dashboard')
@login_required
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    else:
        flash(NOT_LOGGED_IN)
        return redirect(url_for('login')) 

@app.route("/macros")
@login_required
def macros():
    return render_template("macros.html")

@app.route("/workout")
@login_required
def workout():
    return render_template("workout.html")

@app.route("/graphs")
@login_required
def graphs():
    weightlist = db.users.find_one({"username": username})["weightlist"]
    gains = db.users.find_one({"username": username})["gains"] #tracks progress in weights, change name if you want to make it more clear; gains will be a dictionary, for example: {squat: [50, 60, 70], deadlift: [100, 200, 300]}
    return render_template("graphs.html", weightlist=weightlist, gains=gains)

@app.route("/goals")
@login_required
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

@app.route('/login', methods=["GET", "POST"])
def login():
    if 'user' in session:
        flash(ALREADY_LOGGED_IN)
        return redirect(url_for('dashboard'))

    # Logging in
    if request.method == 'POST':
        user = request.form['user']
        pwd = request.form['pwd']

        # Login attempt
        result, passed = mongo.authenticate_user(user, pwd)

        if result: # Success
            session['user'] = user
            flash(passed)
            #redirect(url_for('dashboard'))
            return redirect('dashboard')

        else: # Failure
            flash(passed)
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if 'user' in session:
        flash(ALREADY_LOGGED_IN)
        return redirect(url_for('dashboard'))

    # Registration form submitted
    if request.method == 'POST':
        user = request.form['user']
        pwd = request.form['pwd']

        # Reigstration attempt
        result, passed = mongo.create_user(user, pwd)

        if result: #Success
            flash(passed)
            return redirect(url_for('login'))

        else: # Failure
            flash(passed)
            return redirect(url_for('register'))

    # Viewing registration page
    else:
        return render_template('register.html')

#The original code for register had the following:
#db.users.insert({'name': username, 'password': password, 'weight': 0, 'goal': 'None'})
#Perhaps we should come with our standardized form of storing a user? (what we'll need etc) 
#Until then I'll use a generic one. 

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__=="__main__":
    app.debug=True
    app.run(host = '0.0.0.0')

