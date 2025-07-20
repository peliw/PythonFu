from fastapi import FastAPI
# Multiple path and query parameters
# https://fastapi.tiangolo.com/tutorial/query-params/#multiple-path-and-query-parameters

# creating a fastapi app instance as always
app = FastAPI()

# Function to read user item with optional query parameters
@app.get("/users/{user_id}/items/{item_id}/")

# query paramerets here are optional and are defined by default values
async def read_user_item(
    user_id:int,
    item_id: str, q:str | None = None,
    short:bool = False
    ):
    
    '''
    also function can be written like this:
    async def read_user_item(user_id: int, item_id: str, q: str = None, short: bool = False):
    here for better demonstration we use the first one.
    '''
    
    # first we create a dictionary to hold the item information
    item = {"item id:" : item_id, "iser_id": user_id}

    '''
    if q is not None (means if its presented in the path), it will be added to the item dictionary.
    in second case, if short is True, it will add a message to the item dictionary.
    '''
    if q:
        item.update({"query:" : q})
    if short:
        item.update({"message:" : "This is a short message"})

    # finally, we return the item dictionary
    return item
