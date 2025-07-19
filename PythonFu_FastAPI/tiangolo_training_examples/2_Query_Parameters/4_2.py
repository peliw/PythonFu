from fastapi import FastAPI

# by importing typing we want to use Union for type hinting
from typing import Union

# Multiple path and query parameters
# https://fastapi.tiangolo.com/tutorial/query-params/#multiple-path-and-query-parameters

# creating a fastapi app instance as always
app = FastAPI()

# Function to read user item with optional query parameters
@app.get("/users/{user_id}/items/{item_id}/")
async def read_user_item(
    user_id: int, 
    item_id: str, 
    q: Union[str, None] = None, # Union is used for optional parameters
    short: bool = False
):
    # first we create a dictionary to hold the item information
    item = {"item id": item_id, "user_id": user_id}

    '''
    if q is not None (means if its presented in the path), it will be added to the item dictionary.
    in second case, if short is True, it will add a message to the item dictionary.
    '''
    
    if q:
        item.update({"query": q})
    if short:
        item.update({"message": "This is a short message"})

    # finally, we return the item dictionary
    return item