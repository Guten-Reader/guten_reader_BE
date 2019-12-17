from flask_restful import Resource, reqparse
from models.user import UserModel
# from flask import jsonify

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    def get(self, _id):
        user = UserModel.find_by_id(_id)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def post(self):
        data = User.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()
        return {"message": "User created successfully."}, 201
