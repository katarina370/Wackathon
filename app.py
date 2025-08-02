from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # serves main page

@app.route('/login')
def login():
    return render_template('login.html')  # you can create this later

@app.route('/map')
def map_page():
    return render_template('map.html')  # you can plug in your current map page

if __name__ == '__main__':
    app.run(debug=True)