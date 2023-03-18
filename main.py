from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flask'
app.config['MYSQL_PASSWORD'] = 'flask'
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/database")
def database():
    return render_template('database.html')
    
@app.route("/database/events")
def event():
    cursor = mysql.connection.cursor()
    cursor.execute('select * from place;')
    events = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return render_template('events.html', events=events)

@app.route("/database/events/<id>")
def eventDetails(id):
    cursor = mysql.connection.cursor()
    cursor.execute('select * from place;')
    events = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return render_template('events.html', events=events)
    
@app.route("/database/eventsDashboard")
def eventsDashboard():
    return render_template('eventsDashboard.html') 

@app.route("/database/contactMusician")
def contactMusician():
    return render_template('contactMusician.html')

@app.route("/database/addEvents")
def addEvents():
    return render_template('addEvents.html')

@app.route("/database/volunteers")
def volunteers():
    return render_template('volunteers.html')

@app.route("/database/spectators")
def spectators():
    return render_template('spectators.html')

@app.route("/database/concertHalls")
def concertHalls():
    return render_template('concertHalls.html') 

@app.route("/database/constraint")
def constraint():
    return render_template('constraint.html')

@app.route("/database/contactOrganizer")
def contactOrganizer():
    return render_template('contactOrganizer.html')

@app.route("/database/todo-list")
def todoList():
    return render_template('todo-list.html')

@app.route("/database/validateParticipation")
def validateParticipation():
    return render_template('validateParticipation.html')

@app.route("/database/roomsAvailable")
def roomsAvailable():
    return render_template('roomsAvailable.html')

@app.route("/database/dashboard")
def dashboard():
    return render_template('dashboard.html')  
    

