from flask import Flask, render_template, jsonify, url_for, request, redirect, session
from database import load_records_from_db, get_db_connection
from sqlalchemy import text
import pymysql
from flask import Flask, request, jsonify
from sqlalchemy import create_engine


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/')
def hello():
    return render_template('back.html')

@app.route('/entry', methods=['GET', 'POST'])
def enter_record():
    if request.method=='POST':
        pass

    return render_template('patientEntry.html')

# @app.route('/records', methods=['POST'])
# def add_record():
#     # Get form data
#     name = request.form['name']
#     address = request.form['address']
#     contact = request.form['contact']

#     # Insert data into the MySQL database
#     db = get_db_connection()
#     # query = "INSERT INTO patients (name, address, contact) VALUES (%s, %s, %s)"
#     # db.execute(query, (name, address, contact))
#     query = "INSERT INTO records (name, address, contact) VALUES (:name, :address, :contact)"
#     params = (name, address, contact)  # This should be a tuple
#     db.execute(query, params)
#     db.connection.commit()
#     db.close()

#     return redirect(url_for(''))  # Redirect to a success page or another route

@app.route('/records', methods=['POST'])
def add_record():
    # Get form data
    name = request.form['name']
    address = request.form['address']
    contact = request.form['contact']

    # Insert data into the MySQL database
    session = get_db_connection()
    
    # Creating a new record
    new_record = {
        'name': name,
        'address': address,
        'contact': contact,
        'service':service
    }

    # Using SQLAlchemy to insert the record
    try:
        session.execute(
            "INSERT INTO patient (patient_name, phone) VALUES (:name, :address, :contact)",
            new_record
        )
        session.commit()
        return render_template('success.html'), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/records')
def return_record():
    records = load_records_from_db()
    return render_template('records.html', records=records)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            conn = get_db_connection()
            query = text('SELECT * FROM users WHERE username = :username AND password = :password')
            data = conn.execute(query, {'username': username, 'password': password})
            user = data.fetchone()
        finally:
            conn.close()

        if user:
            session['user_id'] = user.id  # Store user ID in session
            return redirect(url_for('dashboard'))  # Redirect to a dashboard or home page
        else:
            return render_template('login.html', error="Invalid username or password"), 401  # Render with error message

    return render_template('login.html')  # Render the login page for GET requests

@app.route('/dashboard')
def dashboard():
    records = load_records_from_db()
    return render_template("records.html", records=records)

if __name__ == "__main__":
    app.run(debug=True)