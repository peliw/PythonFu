# Required query parameters
# https://fastapi.tiangolo.com/tutorial/query-params/#required-query-parameters
from fastapi import FastAPI

# creating a FastAPI app instance as always
app = FastAPI()

'''
If you don't want to add a specific value but just make it optional, set the default as None.
But when you want to make a query parameter required, you can just not declare any default value:
'''

@app.get("items/{item_id}/")
async def read_item(item_id: int, q: str):
    """
    This function reads an item by its ID and a query parameter.
    The query parameter 'q' is required: required_q.
    """
    item = {"item id": item_id, "required query:": q}
    return item
