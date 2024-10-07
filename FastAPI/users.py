from fastapi import FastAPI
from pydantic import BaseModel

# Iniciar el server: uvicorn users:app --reload
# Detener el server: Ctrl + C

# Entidad user
class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    url: str | None = None
    age: int

app = FastAPI()

users_list = [User(id = 1, first_name = "Geo", last_name = "Manzano", url = "https//geo.com", age = 38),
         User(id = 2, first_name = "Yanet", last_name = "Riquelme", url = "https//riky.com", age = 32)]

@app.get("/users")
async def users():
    return users_list

# Parametros por Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user_by_id(id)

# Parametros por Query
@app.get("/userquery/")
async def user(id: int):
    return search_user_by_id(id)    
    
def search_user_by_id(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}    

@app.post("/users")
async def create_user(user: User):
    return user