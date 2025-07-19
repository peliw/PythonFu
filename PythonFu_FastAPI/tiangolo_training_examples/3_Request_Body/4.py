# Request body + path + query parameters
# https://fastapi.tiangolo.com/tutorial/body/#request-body-path-query-parameters

from fastapi import FastAPI
from pydantic import BaseModel

'''
you declare your data model as a class that inherits from BaseModel.
when a model attribute has a default value,
it is not required, otherwise, it is required.
Use None to make it just optional.
Use standard Python types for all the attributes:
'''

class Item(BaseModel):
    name: str
    description: str | None = None  # --> this line can be difined by Union too
    price: float
    tax: float | None = None        # --> this line can be difined by Union too        

# let's create fastapi instance
app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(
    item_id: int,           # read item_id from the path
    item: Item,             # read item from the request body
    q: str | None = None    # read q from the query parameters (optional, default is None)
    ):

    '''
    FastAPI will recognize that the function parameters that
    match path parameters should be taken from the path,
    and that function parameters that are declared to be
    Pydantic models should be taken from the request body.
    '''

    item_details = {"item_id": item_id, **item.dict()} # **item.dict() usage
    if q: 
        # if q is not None, add it to the item_details
        # if q is None, it will not be added to the item_details
        # this is a way to handle query parameters 
        item_details.update({"q": q})

    return item_details


'''
**item.dict() usage:
The ** operator is dictionary unpacking.
It takes the key-value pairs from item.dict()
and merges them into the outer dictionary.
'''

# following is a sample request you can use it. it uses curl and port proper data to the endpoint
'''
curl -X 'POST' \
  'http://127.0.0.1:8000/items/22' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "description": "string",
  "price": 0,
  "tax": 0
}'
'''