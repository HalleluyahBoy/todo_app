from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime


import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World'

index()


# The get_db_connection() function creates a new connection to the database, 
# and the init_db() function initializes the database by executing a schema file.
def get_db_connection():
    conn = sqlite3.connect('reminders.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with app.open_resource('schema.sql', mode='r') as f:
        conn.executescript(f.read())
    conn.close()

from flask import render_template, request


# create a form for users to add new reminders
@app.route('/add_reminder', methods=['GET', 'POST'])
def add_reminder():
    if request.method == 'POST':
        user_id = request.form['user_id']
        reminder = request.form['reminder']
        date_time = request.form['date_time']

        conn = get_db_connection()
        conn.execute('INSERT INTO reminders (user_id, reminder, date_time) VALUES (?, ?, ?)',
                     (user_id, reminder, date_time))
        conn.commit()
        conn.close()

    return render_template('add_reminder.html')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reminders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)


class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    reminder = db.Column(db.String(255), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Reminder {self.id}>'


@app.route('/add_reminder', methods=['POST'])
def add_reminder():
    user_id = request.json['user_id']
    reminder = request.json['reminder']
    date_time = datetime.fromisoformat(request.json['date_time'])
    new_reminder = Reminder(user_id=user_id, reminder=reminder, date_time=date_time)
    db.session.add(new_reminder)
    db.session.commit()
    return jsonify({'message': 'Reminder added successfully!'})


if __name__ == '__main__':
    app.run(debug=True)

