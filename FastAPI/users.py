from fastapi import FastAPI
from pydantic import BaseModel

# Iniciar el server: uvicorn users:app --reload
# Detener el server: Ctrl + C

# Entidad user
class User(BaseModel):
    first_name: str
    last_name: str
    url: str
    age: int

app = FastAPI()

users_list = [User(first_name = "Geo", last_name = "Manzano", url = "https//geo.com", age = 38),
         User(first_name = "Yanet", last_name = "Riquelme", url = "https//riky.com", age = 32)]

@app.get("/users")
async def users():
    return users_list