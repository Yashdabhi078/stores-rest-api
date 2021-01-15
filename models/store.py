from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    # items = db.relationship('ItemModel')    # this works like a join..it will do -> ItemModel*StoreModel and only matched id items row will be fetched -> hence return list of items objects
    items = db.relationship('ItemModel',lazy="dynamic")    # -> so in exact above line it will create all items objects and return it..it loads too much..,,so we do lazy="dynamic" means only return items obj. when it will be called by .all()
    
    def __init__(self,name): 
        self.name = name
        
    def json(self):
        return {"name":self.name,"items":[item.json() for item in self.items.all()]}  # here we called items using .all() so..now it will create object and     fetch items
    
    @classmethod   
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
        
    def save_to_db(self):
        db.session.add(self)    
        db.session.commit()     
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()