from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle form submissions
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f'Hello, {name}! Welcome to Flask Web App.'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
