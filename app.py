from db import db
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,ItemList
from resources.store import Store,StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" #database file store in root of the folder (/data.db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # SQLAlchemy has modification tracket that use resources..so we make it off but SQLAlchemy has its own tracker library that is much better ..hence we use it. [so its only change extention behaviour not SQLAlchemy behaviour]
app.secret_key = 'jose'
api = Api(app)      #it will allow us to add resourse..and every Resource Must be Class


# app.config['JWT_AUTH_URL_RULE'] = '/login'    ## if want to change from '/auth' to 'login' in below/....
jwt = JWT(app,authenticate,identity)    ## /auth ->> htts://127.0.0.1:5000/auth -> with this request we have to send uid,pwd then it will go inside 'Authorization' and if user found then retern "JWT TOKEN",, which need to send with (Payload) in 'Authentication' header every time when we try to access "@JWT_required()" methods..(get,post..etc..)  

## more about JWT...
# https://blog.tecladocode.com/learn-python-advanced-configuration-of-flask-jwt/
    
api.add_resource(Item,'/item/<string:name>')   #htts://127.0.0.1:5000/sudent/yash -> if we search this,it will call Student GET/POST mothod as per request
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)