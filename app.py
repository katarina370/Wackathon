from flask import Flask, render_template

app = Flask(__name__)

# route for main/landing page
@app.route('/')
def home():
    return render_template('index.html')  # serves main page

# route for login page
@app.route('/login')
def login():
    # login stuff here
    return render_template('login.html')

# route for map page
@app.route('/map')
def map_page():
    return render_template('map_interface.html')

if __name__ == '__main__':
    app.run(debug=True)