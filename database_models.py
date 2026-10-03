#models for database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

import database

Base=declarative_base()     # Python class/model name

class Product(Base):    # database table name       

    __tablename__="product"
    id= Column(Integer, primary_key=True, index=True)       #columns 
    name= Column(String, index=True)