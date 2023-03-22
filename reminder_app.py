import sqlite3
from flask import Flask, render_template, request, g, redirect, url_for

# Database initialization
DATABASE = 'reminders.db'


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row

    return g.db

def get_db_connection():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())

        # Add this line to drop the "reminders" table if it exists
        db.cursor().execute("DROP TABLE IF EXISTS reminders")
        
        db.commit()


# Flask app initialization
app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='dev')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Routes
@app.route('/')
def index():
    cur = get_db_connection().cursor()
    cur.execute('SELECT * FROM reminders')
    reminders = cur.fetchall()
    cur.close()
    return render_template('index.html', reminders=reminders)

@app.route('/add_reminder', methods=('GET', 'POST'))
def add_reminder():
    if request.method == 'POST':
        user_id = request.form['user_id']
        reminder = request.form['reminder']
        date_time = request.form['date_time']

        cur = get_db_connection().cursor()
        cur.execute('INSERT INTO reminders (user_id, reminder, date_time) VALUES (?, ?, ?)', (user_id, reminder, date_time))
        get_db_connection().commit()
        cur.close()
        return redirect('/')

    return render_template('add_reminder.html')

@app.route('/edit_reminder/<int:id>', methods=('GET', 'POST'))
def edit_reminder(id):
    cur = get_db_connection().cursor()
    cur.execute('SELECT * FROM reminders WHERE id = ?', (id,))
    reminder = cur.fetchone()
    cur.close()

    if request.method == 'POST':
        user_id = request.form['user_id']
        reminder_text = request.form['reminder']
        date_time = request.form['date_time']

        cur = get_db_connection().cursor()
        cur.execute('UPDATE reminders SET user_id = ?, reminder = ?, date_time = ? WHERE id = ?', (user_id, reminder_text, date_time, id))
        get_db_connection().commit()
        cur.close()

        return redirect('/')
    
    return render_template('edit_reminder.html', reminder=reminder)

@app.route('/delete_reminder/<int:id>')
def delete_reminder(id):
    cur = get_db_connection().cursor()
    cur.execute('DELETE FROM reminders WHERE id = ?', (id,))
    get_db_connection().commit()
    cur.close()

    return redirect('/')

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# App initialization
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
