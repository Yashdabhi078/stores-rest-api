from app import app
from db import db

db.init_app(app)

@app.before_first_request   # but it will work little bit slower..copare to sqlite
def create_tables():
    db.create_all() #will create all table taht is here or inside the class which is imported
