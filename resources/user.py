import sqlite3
from flask_restful import Resource, reqparse
from models.usermodel import UserModel



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Cannot be empty"
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Cannot be empty"
                        )

    def post(self):
        user_details = UserRegister.parser.parse_args()
        if UserModel.find_by_username(user_details['username']):
            return {"message": "User Already exits"}, 401
        user = UserModel(**user_details)
        user.save_to_db()
        return {"message": "user registered successfully"}, 201
