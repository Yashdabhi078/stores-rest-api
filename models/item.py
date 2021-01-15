# import sqlite3
from db import db

class ItemModel(db.Model):  #here extend bcz..we told that obj of this class is directy connected to database,,means for as we create new object it willstore it into database
    __tablename__ = "items"
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2)) # after point(0.00) 2 digit
    
    store_id =db.Column(db.Integer,db.ForeignKey('stores.id'))  # take reference of 'id' column inside 'stores' table
    store = db.relationship('StoreModel')   # founded store id will match the id inside 'StoreModel' database
    # how it works :- SQLAlchemy directly recive the data from table and pump it into beow init metho for each row..so it will create objects for each row automatically
    
    def __init__(self,name,price,store_id):     # hence,its direct connection between database and object.
        self.name = name
        self.price = price
        self.store_id = store_id
        
    def json(self):
        return {"name":self.name,"price":self.price}
    
    @classmethod   
    def find_by_name(cls,name):
        return cls.query.filter_by(name = name).first()       # SELECT * FROM __tablename__ WHERE name=name LIMIT 1  ##-->return ItemModel.query.filter_by(name = name).filter_by(id=1)  ##--> return ItemModel.query.filter_by(name = name,id=1)
        #here ..it will return an ItemModel 'Object'..as ItemModel and SQLAlchemy database connected so..
        
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        
        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query,(name,))
        # row = result.fetchone()         # retriving item from database
        # connection.close()
        
        # if row:
        #     return cls(*row)
        #     # return {"item":{"name":row[0],"price":row[1]}}
    
    def save_to_db(self):
        db.session.add(self)    # as it directly connected..object we have directly stored into database..
        db.session.commit()     
        # it will insert as well as update,,both will done in the same...as we have id as a primary key
        
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        # query = "INSERT INTO items VALUES(?,?)"
        # cursor.execute(query,(self.name,self.price))
        # connection.commit()
        # connection.close()
        
    # def update(self):
    #     connection = sqlite3.connect("data.db")
    #     cursor = connection.cursor()
    #     query = "UPDATE items set price=? WHERE name=?"
    #     cursor.execute(query,(self.price,self.name))
            
    #     connection.commit()
    #     connection.close()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()