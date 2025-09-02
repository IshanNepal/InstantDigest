import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env into environment

class Config:
     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///default.db")
     SQLALCHEMY_TRACK_MODIFICATIONS = False
    
