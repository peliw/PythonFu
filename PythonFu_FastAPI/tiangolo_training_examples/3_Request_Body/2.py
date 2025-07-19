# Use the model
# https://fastapi.tiangolo.com/tutorial/body/#use-the-model

from fastapi import FastAPI
from pydantic import BaseModel # in this example you need to import BaseModel from pydantic

# as previous example Item is a class-based model defined first
class Item(BaseModel):
    name: str
    description: str | None = None # --> this line can be difined by Union too
    price: float
    tax: float | None = None # --> this line can be difined by Union too


# as always we will create an instance of fastap app
app = FastAPI()

# inside of the function, you can access all the attributes of the model object directly
@app.post("/items/")
async def create_item(item: Item):

    ''' 
    following line is used to convert a Pydantic model instance (item)
    into a standard Python dictionary:
    Common Use Cases:
        - Serializing the data to JSON (e.g., json.dumps(item.dict()))
        - Sending data to a database
        - Logging or debugging
        - Returning modified data in a response
    '''
    item_dict = item.dict()

    # following we will use predefined pydantic basemodel in the funtion
    if item.tax is not None:
        price_with_tax = item.price + (item.tax * item.price)
        item_dict.update({"price_with_tax" : price_with_tax})

    return item_dict



# following is a sample request you can use it. it uses curl and port proper data to the endpoint
'''
curl -X 'POST' \
  'http://127.0.0.1:8000/items' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "description": "string",
  "price": 0,
  "tax": 0
}'
'''