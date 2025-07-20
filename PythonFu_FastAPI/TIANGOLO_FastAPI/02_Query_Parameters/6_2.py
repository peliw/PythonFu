# Required query parameters
# https://fastapi.tiangolo.com/tutorial/query-params/#required-query-parameters
from fastapi import FastAPI
from typing import Union
app = FastAPI()

'''
of course, you can define some parameters as required,
some as having a default value, and some entirely optional.

in following example the code is as practice no.6 and it has used Union
'''

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, # this is required path parameter
    needy: str, # this is required query parameter
    skip: int = 0, # this is a query parameter with default value = 0
    limit: Union[int, None] = None # this is optional query parameter with default value = None, note to using Union here
):

    # following dictionary includes all parameters we defined, optionals and requireds
    item = {
        "item_id": item_id,
        "needy": needy,
        "skip": skip,
        "limit": limit
    }

    # let's see the output once we deliver optional and required parameter to the app
    return item