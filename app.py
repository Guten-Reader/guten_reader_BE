from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# @app.route('/')
# def hello():
#     return 'Guten-Reader API'

class User(Resource):
    def get(self, name):
        return {'user': name}

api.add_resource(User, '/users/<string:name>')

if __name__ == '__main__':
    app.run(port=5000)
