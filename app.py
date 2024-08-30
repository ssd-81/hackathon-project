from flask import Flask, render_template , jsonify 

app = Flask(__name__)

JOBS = [ # type: ignore
    {
        'id': 1,
        'title':'Data analyst',
        'location':'delhi,India',
        'salary':'10,00,000',
    },
    {
        'id': 2,
        'title':'Data scientist',
        'location':'bengluru,India',
        'salary':'15,00,000',
    },
    {
        'id': 3,
        'title':'Frontend engineer.',
        'location':'hydrabad,India',
        'salary':'12,00,000',
    },
    {
        'id': 4,
        'title':'Backend engineer',
        'location':'stanford,USA',
        'salary':'$32,000',
    },
    ]

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