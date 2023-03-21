from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/database")
def database():
    return render_template('database.html')
    
@app.route("/database/events")
def events():
    return render_template('events.html', events=events)
    
@app.route("/database/eventsDashboard")
def eventsDashboard():
    return render_template('eventsDashboard.html') 

@app.route("/database/contactMusician")
def contactMusician():
    return render_template('contactMusician.html')

@app.route("/database/dashboardOrga")
def dashboardOrga():
    return render_template('dashboardOrga.html')

@app.route("/database/spectators")
def spectators():
    return render_template('spectators.html')

@app.route("/database/constraint")
def constraint():
    return render_template('constraint.html')

@app.route("/database/roomsAvailable")
def roomsAvailable():
    return render_template('roomsAvailable.html')

@app.route("/database/dashboard")
def dashboard():
    return render_template('dashboard.html')  
    

