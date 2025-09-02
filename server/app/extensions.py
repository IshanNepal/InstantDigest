from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

'''Creating Instances'''
db = SQLAlchemy()
cors = CORS()

'''Func for Initializing Extentions'''
def init_extentions(app):
    db.init_app(app)
    cors.init_app(app)