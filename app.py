from flask import Flask
from flask_restful import Api
from resources.user import User
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/guten_reader_dev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

logging.info("Doing something!")

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(User, '/users', '/users/<int:_id>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
