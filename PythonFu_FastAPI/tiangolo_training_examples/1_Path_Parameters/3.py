from fastapi import FastAPI
# Order matters

app = FastAPI()

# Similarly, you cannot redefine a path operation:

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]