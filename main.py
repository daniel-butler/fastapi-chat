from fastapi import FastAPI

app = FastAPI()

fake_db_items = [{"item_name": "truck"}, {"item_name": "airplane"}, {"item)_name": "dolphin"}]


@app.get("/items/")
async def read_item(skip:int = 0, limit: int = 10):
    return fake_db_items[skip : skip + limit]
