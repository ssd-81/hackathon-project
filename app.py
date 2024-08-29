from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/home')
def show_home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)