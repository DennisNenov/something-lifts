from flask import Flask,render_template, session, redirect, request, url_for, g, flash
from functools import wraps
import tools
import auth
import urllib2
import json

app = Flask(__name__)
app.secret_key = "a"

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
        gains = tools.getAllLifts(session['user'])
        return render_template('dashboard.html', gains=gains)
    else:
        flash(NOT_LOGGED_IN)
        return redirect(url_for('login')) 

@app.route("/macros", methods=["GET", "POST"])
@login_required
def macros():
    if request.method == "POST":
        if "choosefood" in request.form:
            user = session['user']
            date = request.form.get("date")
            servings = request.form.get("servings")
            calories = str(float(servings)*float(request.form.get("calories")))
            fat = str(float(servings)*float(request.form.get("fat")))
            carbs = str(float(servings)*float(request.form.get("carbs")))
            protein = str(float(servings)*float(request.form.get("protein")))
            tools.enterFood(user, date, calories, fat, carbs, protein)
            #return str(tools.getFood(user, date))
            flash("Food input successful")
            return redirect(url_for("dashboard"))
        date = request.form.get("date", None)
        food = request.form.get("food", None)
        if date==None or date=="" or food==None or food=="":
            flash("Please input values for the date and food")
            return redirect(url_for("dashboard"))
        else:
            url = urllib2.urlopen("https://api.damonmcminn.com/nutrition/food?search=" + food.replace(" ", "-"))
            d = json.load(url)['foods']
    return render_template("macros.html", d=d, date=date)

@app.route("/stats")
@login_required
def stats():
    user = session['user']
    gains = tools.getAllLifts(user)
    foodstuff = tools.getAllFood(user)
    #avgc = foodstuff["calories"]/foodstuff["numDates"]
    liftnames = gains.keys();
    lifts = gains.values();
    start = 0
    avgs = []
    orm = []
    while start < len(lifts):
        avgs.append(tools.getAvgROC(lifts[start]))
        orm.append((max(lifts[start]))/.8)
        start+=1
    return render_template("stats.html", avgs=avgs, liftnames=liftnames, orm=orm)

@app.route("/workout")
@login_required
def workout():
    return render_template("workout.html")

@app.route("/enter", methods=["GET", "POST"])
@login_required
def enter():
    if request.method == "POST":
        try:
            lifts = {}
            print request.form
            for i in range(len(request.form)/2):
                lifts[request.form.get('lift'+str(i+1))] = int(request.form.get('amount'+str(i+1)))
            user = session['user']
        except:
            flash("Please input valid values for lifts and amounts")
            return redirect(url_for("dashboard"))
        print "HELLO"
        print "lifts: " + str(lifts)
        tools.enterInfo(user, lifts)
        return redirect(url_for("dashboard"))
    else:
        return "You are not supposed to be here"

@app.route("/graphs/<graph>", methods=["GET", "POST"])
#@login_required
def graphs(graph):
    user = session['user']
    gains = tools.getAllLifts(user)
    if graph=="lift":
        workoutNumber = request.form.get("workoutNumber")
        lifts = tools.getLifts(user, workoutNumber)
        return render_template("lifts.html", lifts=lifts)
    if graph=="food":
        date = request.form.get("date")
        food = tools.getFood(user, date)
        return render_template("food.html", food=food)
    return render_template("graphs.html", weightlist=gains[graph], graph=graph)

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

@app.route("/bodyweight", methods=["POST"])
def weight():
    try:
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        age = float(request.form["age"])
        gender = request.form["gender"]
    except:
        return "Please enter numbers for weight, height, and age"
    if gender == "Male":
        tdee = 10 * weight / 2.2 + 6.25 * height * 2.54 - 5 * age + 5
    elif gender == "Female":
        tdee = 10 * weight / 2.2 + 6.25 * height * 2.54 - 5 * age - 161
    protein = weight / 2.2
    fat = weight / 2
    return render_template("bodyweight.html", weight=weight, tdee=tdee, protein=protein, fat=fat)

@app.route("/about")
def about():
    return render_template("about.html")

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
        result, passed = auth.authenticate_user(user, pwd)

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
        result, passed = auth.create_user(user, pwd)

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

