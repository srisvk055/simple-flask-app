from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello World! testing flask app"

@app.route('/hello')
def hello():
    return 'I am good, how about you?'

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
