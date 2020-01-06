from flask import Flask

app = Flask(__name__)

from project import routes


app.run(port=5000, debug=True)