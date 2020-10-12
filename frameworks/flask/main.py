from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/usuario')
def regresa_usuario():
    return {"nombre":"Juan", "edad":29}

app.run()