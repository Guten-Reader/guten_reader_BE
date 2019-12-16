from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Guten-Reader API'

app.run(port=5000)