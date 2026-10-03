from fastapi import FastAPI
from models import Product
from database import session, engine
import database_models

app=FastAPI()

database_models.Base.metadata.create_all(bind=engine)   #create table in database


@app.get("/")
def greet():
    return "Hi i am function!"

Products=[
    Product(id=1, name="product1"),
    Product(id=2, name="product2"),
    Product(id=3, name="product3")

]

def init_db():
    db=session()

    for product in Products:
        db.add(database_models.Product(**product.model_dump()))   #add product to database
    db.commit()

init_db()   #call init_db function to add products to database

@app.get("/products")
def get_products():
    db=session()        #db connection
    db.query()      #query
    return Products


@app.get("/product/{id}")
def product_id(id:int):
    for product in Products:
        if product.id==id:
            return product

    print("Product not found")

@app.post("/product")
def add_product(product:Product):
    Products.append(product)
    return product

@app.put("/product")
def update_product(id:int, product:Product):
    for i in range(len(Products)):
        if Products[i].id==id:
            Products[i]=product
            return "product updated successfully"

    return "product not found"


@app.delete("/product/")
def delete_product(id:int):
    for i in range(len(Products)):
        if Products[i].id==id:
            Products.pop(i)
            return "product deleted successfully"

    return "product not found"