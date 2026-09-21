from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def greet():
    return "Welcome to Telusko Trac"



@app.get("/products")
def get_products():
    return "products"