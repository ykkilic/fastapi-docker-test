from fastapi import FastAPI
import os

app = FastAPI()

ENDPOINT = os.getenv("ENDPOINT")

if ENDPOINT == "user":
    @app.get("/user/{user_id}")
    async def read_user(user_id: int):
        return {"message" : f"User {user_id}"}

elif ENDPOINT == "product":
    @app.get("/product/{product_id}")
    async def read_product(product_id: int):
        return {"message" : f"Product {product_id}"}

else:
    @app.get("/")
    async def read_root():
        return {"message": "Hello World"}