# import sqlite3 
from flask_jwt import jwt_required
from flask_restful import Resource,reqparse
from models.item import ItemModel

class Item(Resource):    # Student is resource -> whence ,e can call resourse
    
    parser = reqparse.RequestParser()   #it can parse both form and json() payload .. here we can fetch only those element which is required from the recived json response.
    parser.add_argument(
        'price',                # here we take only price args..from recived json payload..and ignore others..
        type = float,
        required = True,
        help = "this filed cant be left black!!"            ## if 'price' not found then this msg will return..
    )
    parser.add_argument(
        'store_id',                # here we take only price args..from recived json payload..and ignore others..
        type = int,
        required = True,
        help = "Every item need a store id!"            ## if 'price' not found then this msg will return..
    )
    
    @jwt_required()     #for access below mwthod ,authentcation is required
    def get(self,name):     # will call this method when GET request for this resourse fired..
        item =ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            {"message":"Item not found"},404
        
    
    def post(self,name):
        if ItemModel.find_by_name(name): #check item exist or not
            return {"message":"An item with name '{}' is already exists.".format(name)},400 # 400 Bad requests
        
        # item not alredy exist so we create new
        data = Item.parser.parse_args()
        item = ItemModel(name,**data) #data["price"],data["store_id"]
        try:
            item.save_to_db()
        except:
            return {"message":"an error occured interting item."},500   #internal server error
        return item.json(),201
        
    
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item is None:    #check item exist or not
            return {"message":"Item not found for deletion"},404
        else :
            item.delete_from_db()
            return {"message" : "item deleted"}
        
        
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query,(name,))
        # connection.commit()
        # connection.close()
        
        # return {"message":"item is deleted succesfully"}
    
    def put(self,name):     
        data = Item.parser.parse_args()
        
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name,**data) #data["price"],data["store_id"]
        else:
            item.price = data["price"]
        
        item.save_to_db()
        return item.json(),201
            
         

class ItemList(Resource):
    def get(self):
        result = ItemModel.query.all()  # return list of objects og ItemModel class
        items = [item.json() for item in result]
        return {"items":items}
        
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        # query = "SELECT * FROM items"
        # rows = cursor.execute(query)
        # items = [{"name":row[0],"price":row[1]} for row in rows]
        # return {"items":items}
        # connection.close()