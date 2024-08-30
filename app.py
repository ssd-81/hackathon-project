from flask import Flask, render_template , jsonify 
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('login.html')


@app.route('/entry')
def enter_record():
    return render_template('patientEntry.html')

@app.route('/records')
def return_record():
    return render_template('records.html')

if __name__ == "__main__":
    app.run(debug=True)