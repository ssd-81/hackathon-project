from flask import Flask, render_template , jsonify 
import sqlalchemy
from flask import url_for
from database import load_records_from_db


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('page1.html')


@app.route('/entry')
def enter_record():
    return render_template('patientEntry.html')

@app.route('/records')
def return_record():
    records = load_records_from_db()
    return render_template('records.html', records=records)

@app.route('/home')
def home():
    return render_template('back.html')

if __name__ == "__main__":
    app.run(debug=True)