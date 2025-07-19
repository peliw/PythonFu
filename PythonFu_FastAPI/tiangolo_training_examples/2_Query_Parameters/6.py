# Required query parameters
# https://fastapi.tiangolo.com/tutorial/query-params/#required-query-parameters
from fastapi import FastAPI

app = FastAPI()

'''
of course, you can define some parameters as required,
some as having a default value, and some entirely optional
'''

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, # this is required path parameters
    needy: str, # this is required query parameters
    skip: int = 0, # this is required query parameters with default value = 0
    limit: int | None = None # this is optional query parameters with default value = None
):
    item = {
        "item_id": item_id,
        "needy": needy,
        "skip": skip,
        "limit": limit
    }

    # let's see the output once we deliver optional and required parameter to the app
    return item