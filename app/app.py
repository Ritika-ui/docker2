from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Mini Challenge Success! 🚀"

@app.route('/hello')
def hello():
    return "Hello from your container!"



app.run(host='0.0.0.0', port=5000)
