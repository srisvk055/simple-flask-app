from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def main():
<<<<<<< HEAD
    return "Hello World! testing flask app"
=======
    return "Hello World!"
>>>>>>> f571548abd8deec137b461dceb65a5d00811d81f

@app.route('/hello')
def hello():
    return 'I am good, how about you?'

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
