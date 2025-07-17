from fastapi import FastAPI

app = FastAPI()
# And of course, you can define some parameters as required, some as having a default value, and some entirely optional:

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item