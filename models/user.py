# import sqlite3
from db import db

class UserModel(db.Model):     # for Login     # not a resource,call via JWT->security
    __tablename__ = "users"     # we tell SQLAlchemy that ..this is the table name where object data is going to store
    
    id  = db.Column(db.Integer,primary_key = True)  # told SQLAlchemy that , a clm name id which is Primary key
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    
    
    def __init__(self,username,password):
        # self.id =_id  #in SQLAlchemy it automatic assign id and also its auto incrememting..hence we remove id from here
        self.username=username
        self.password=password
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()   # here .. [ cls.query -> select * from users ]
        
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        
        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query,(username,))
        # row = result.fetchone()
        # if row:
        #     user = UserModel(*row)
        # else :
        #     user = None
        
        # connection.close()
        # return user
    
    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first()
    
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        
        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query,(_id,))
        # row = result.fetchone()
        # if row:
        #     user = UserModel(*row)
        # else :
        #     user = None
        
        # connection.close()
        # return user
    