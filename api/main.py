import os
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from datetime import date
from fastapi import FastAPI, HTTPException
from typing import List


class Videojuego(BaseModel):
    gameid: str
    titulo: str
    plataforma: str
    genero: str
    desarrollador: str
    fecha: date # Formato: YYYY-MM-DD

app = FastAPI()

MONGO_URL = os.getenv("MONGO_URL")
client = AsyncIOMotorClient(MONGO_URL)
db = client["videojuegos"]

@app.get("/")
async def root():
    return {"ok": True, "Colecciones": await db.list_collection_names()}


#Endpoint para listar todos los juegos
@app.get("/juegos", response_description="Lista de juegos", response_model=List[Videojuego])
async def listar_juegos():
    juegos = await db["juegos"].find().to_list(1000)
    return juegos

#Endpoint para agregar juegos
@app.post("/juegos", response_description="Agregar nuevo juego", response_model=Videojuego)
async def agregar_juego(juego: Videojuego):
    juego_dict = juego.dict()
    juego_dict["fecha"] = juego.fecha.isoformat()
    await db["juegos"].insert_one(juego_dict)
    return juego

#Endpoint para obtener los datos de un juego por su 'gameid'
@app.get("/juegos/{gameid}", response_description="Obtener datos de un juego", response_model=Videojuego)
async def obtener_juego(gameid: str):
    juego = await db["juegos"].find_one({"gameid": gameid})   
    if juego is not None:
        return juego
    else:
        raise HTTPException(status_code=404, detail=f"Juego con 'gameid' {gameid} no encontrado")

#Endpoint para remover un juego por su 'gameid'
@app.delete("/juegos/{gameid}", response_description="Eliminar un juego")
async def eliminar_juego(gameid: str):
    juego = await db["juegos"].find_one({"gameid": gameid})
    if juego is not None:
        await db["juegos"].delete_one({"gameid": gameid})
        return {"message": f"Juego con 'gameid' {gameid} eliminado correctamente."}
    else:
        raise HTTPException(status_code=404, detail=f"Juego con 'gameid' {gameid} no encontrado")
    
#Endpoint para actualizar los datos de un juego por su 'gameid'
@app.put("/juegos/{gameid}", response_description="Actualizar un juego", response_model=List[Videojuego])
async def actualizar_juego(gameid: str, juego: Videojuego):
    juego_dict = juego.dict()
    juego_dict["fecha"] = juego.fecha.isoformat()
    result = await db["juegos"].update_one({"gameid": gameid}, {"$set": juego_dict})
    if result.modified_count == 1:
        await db["juegos"].find_one({"gameid": gameid})
        return await listar_juegos()
    else:
        raise HTTPException(status_code=404, detail=f"Juego con 'gameid' {gameid} no encontrado")

#Endpoint para listar juegos por género
@app.get("/juegos/genero/{genero}", response_description="Lista de juegos por género", response_model=List[Videojuego])
async def listar_por_genero(genero: str):
    juegos = await db["juegos"].find({"genero": genero}).to_list(1000)
    return juegos