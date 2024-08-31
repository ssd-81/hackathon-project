from flask import Flask, render_template , jsonify, url_for,request, redirect, session
from database import load_records_from_db, get_db_connection
import mysql.connector



app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('back.html')


@app.route('/entry')
def enter_record():
    return render_template('patientEntry.html')

@app.route('/records')
def return_record():
    records = load_records_from_db()
    return render_template('records.html', records=records)

# @app.route('/login')
# def home():
#     return render_template('page1.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Query to check if the user exists
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            session['user_id'] = user['id']  # Store user ID in session
            return redirect(url_for('dashboard'))  # Redirect to a dashboard or home page
        else:
            return "Invalid username or password", 401  # Return an error message
    return render_template('page1.html')  # Render the login page

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in
    return "Welcome to your dashboard!"

if __name__ == "__main__":
    app.run(debug=True)