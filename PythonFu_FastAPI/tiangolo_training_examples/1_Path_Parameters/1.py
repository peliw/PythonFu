from fastapi import FastAPI
# Path Parameters
app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}