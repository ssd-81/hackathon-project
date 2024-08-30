from flask import Flask, render_template , jsonify 
from flask import url_for
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def load_records_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from p"))
        result_all = result.all()
        result_dicts = []
        for row in result_all:
            result_dicts.append(dict(dict(row._mapping)))

@app.route('/')
def hello():
    return render_template('login.html')


@app.route('/entry')
def enter_record():
    return render_template('patientEntry.html')

@app.route('/records')
def return_record():
    records = load_records_from_db()
    return render_template('records.html', records=records)

if __name__ == "__main__":
    app.run(debug=True)