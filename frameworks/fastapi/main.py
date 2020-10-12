from fastapi import FastAPI
app = FastAPI()
from modelos import Item

@app.get("/")
def read_root():
    """ Regresa la función raíz. """
    return {"Hello": "World"}

@app.post("/user" , tags=["User"])
def insertar_nuevo_usuario():
    """ """
    return {"user": "juan"}

@app.post("/item" , tags=["Elemento"])
def insertar_nuevo_usuario(item : Item):
    """ """
    return {"user": "juan"}