import os
import psycopg2
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

def get_db_connection():
    connect = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return connect


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route("/database", methods=['GET'])
def database():
    if request.method == 'GET':
        return render_template('database.html')
    
@app.route("/database/ticketing", methods=['GET'])
def ticketing():
    if request.method == 'GET':
        connect = get_db_connection()
        cur = connect.cursor()
        cur.execute('SELECT * FROM ticket;')
        tickets = cur.fetchall()
        print(tickets)
        cur.close()
        connect.close()
        return render_template('ticketing.html', tickets=tickets)

@app.route("/database/events", methods=['GET'])
def events():
    if request.method == 'GET':
        connect = get_db_connection()
        cur = connect.cursor()
        cur.execute('SELECT * FROM event;')
        events = cur.fetchall()
        print(events)
        cur.close()
        connect.close()
        return render_template('events.html', events=events)

@app.route("/database/musicalGroups", methods=['GET'])
def musicalGroups():
    if request.method == 'GET':
        connect = get_db_connection()
        cur = connect.cursor()
        cur.execute('SELECT * FROM musicians;')
        musicians = cur.fetchall()
        print(musicians)
        cur.close()
        connect.close()
        return render_template('musicalGroups.html', musicians=musicians)
    
@app.route("/database/eventsDashboard", methods=['GET'])
def eventsDashboard():
    if request.method == 'GET':
        return render_template('eventsDashboard.html') 

@app.route("/database/contactMusician", methods=['GET'])
def contactMusician():
    if request.method == 'GET':
        return render_template('contactMusician.html')

@app.route("/database/addEvents", methods=['GET'])
def addEvents():
    if request.method == 'GET':
        return render_template('addEvents.html')

@app.route("/database/volunteers", methods=['GET'])
def volunteers():
    if request.method == 'GET':
        return render_template('volunteers.html')

@app.route("/database/spectators", methods=['GET'])
def spectators():
    if request.method == 'GET':
        return render_template('spectators.html')

@app.route("/database/concertHalls", methods=['GET'])
def concertHalls():
    if request.method == 'GET':
        return render_template('concertHalls.html') 

@app.route("/database/constraint", methods=['GET'])
def constraint():
    if request.method == 'GET':
        return render_template('constraint.html')

@app.route("/database/contactOrganizer", methods=['GET'])
def contactOrganizer():
    if request.method == 'GET':
        return render_template('contactOrganizer.html')

@app.route("/database/todo-list", methods=['GET'])
def todoList():
    if request.method == 'GET':
        return render_template('todo-list.html')

@app.route("/database/validateParticipation", methods=['GET'])
def validateParticipation():
    if request.method == 'GET':
        return render_template('validateParticipation.html')

@app.route("/database/roomsAvailable", methods=['GET'])
def roomsAvailable():
    if request.method == 'GET':
        return render_template('roomsAvailable.html')

@app.route("/database/dashboard", methods=['GET'])
def dashboard():
    if request.method == 'GET':
        return render_template('dashboard.html')  
    