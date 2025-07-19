# Request body + path param
# https://fastapi.tiangolo.com/tutorial/body/#request-body-path-parameters

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

    description: str | None = None  # --> this line can be difined by Union too:
                                    # description: Union[str, None] = None
    price: float

    tax: float | None = None        # --> this line can be difined by Union too:
                                    # tax: Union[float, None] = None 
        

# let's create fastapi instance
app = FastAPI()

'''
FastAPI will recognize that the function parameters that
match path parameters should be taken from the path,
and that function parameters that are declared to be
Pydantic models should be taken from the request body.
'''

@app.post("/items/{user_id}")
async def update_item(user_id: int, item: Item):
    # user_items = {"user id": user_id}
    return {"user_id": user_id, **item.dict()}

'''
**item.dict() usage:
The ** operator is dictionary unpacking.
It takes the key-value pairs from item.dict()
and merges them into the outer dictionary.
'''