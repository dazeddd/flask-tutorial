from flask import Flask

app = Flask(__name__)

@app.rount('/')
def hello():
    return 'Hello World'