from fastapi import FastAPI, Path,Query
from pydantic import BaseModel

app = FastAPI()

class Gamed(BaseModel):
    ids:int 
    gamenamez:str
    
@app.get("/home")
def home():
    return {"Hello": "World"}

@app.get("/")
def about():
    return {"Creator":"Arjun",
            "skills":"python",
            "about":"I am a python developer from chennai"}
    


inventory = {
    1:{"name":"laptop","price":50000},
    2:{"name":"mobile","price":10000},
    3:{"name":"tv","price":20000},
    4:{"name":"fridge","price":30000}
}

games = {"games":{1:"GTA5",
                     2:"Warzone",
                     3:"valorant",
                     4:"forest"}}

#positional parameter example
@app.get("/get-item/{item_id}")
def get_item(item_id:int):
    return inventory[item_id]

@app.get("/arthemetic/{number1}")
def get_item(number1:int = Path(None,description="Enter the number to add with 10")):
    return number1 + 10


# Query parameters example
@app.get("/game")
def get_item(*,gamename:str = None):
    for gameid in games["games"]:
        if games["games"][gameid] == gamename:
            return {"gameid":gameid,"gamename":gamename}
    return games["games"]

#request body and post method
@app.post("/create-game")
def create_item(game : Gamed):
    if game.ids in games["games"]:
        return {"error":"game id already exists"}
    
    games["games"][game.ids] = game.gamenamez
    return "inserted"

#put method
@app.put("/update-game")
def update_game(game:Gamed):
    if game.ids not in games["games"]:
        return {"error":"game id does not exists"}
    
    dicti = {game.ids:game.gamenamez}
    games["games"].update(dicti)
    return "updated"