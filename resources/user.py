import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):   # for new sign up   # making it resource
    
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required =True,
        help = "This field can't left empty!!"
    )
    parser.add_argument(
        "password",
        type=str,
        required =True,
        help = "This field can't left empty!!"
    )


    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data["username"]):
            return {"message" : "user alredy exists !!"},400
        
        user = UserModel(**data)  #data["username"],data["password"]
        user.save_to_db()
        return {"message" : "User created successfully"},201
        
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        
        # query = "INSERT INTO users VALUES (NULL,?,?)"
        # cursor.execute(query,(data["username"],data["password"]))
        
        # connection.commit()
        # connection.close()
        
        