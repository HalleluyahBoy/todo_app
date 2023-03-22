import sqlite3
from flask import Flask, render_template, request, g, redirect, url_for

app = Flask(__name__)

DATABASE = 'reminders.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.teardown_appcontext
def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    db = get_db()
    reminders = db.execute('SELECT * FROM reminders').fetchall()
    return render_template('index.html', reminders=reminders)

@app.route('/add', methods=['POST'])
def add_reminder():
    reminder = request.form['reminder']
    date_time = request.form['date_time']
    db = get_db()
    db.execute('INSERT INTO reminders (user_id, reminder, date_time) VALUES (?, ?, ?)', (1, reminder, date_time))
    db.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_reminder(id):
    db = get_db()
    db.execute('DELETE FROM reminders WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
