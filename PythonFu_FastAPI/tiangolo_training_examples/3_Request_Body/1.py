# Import Pydantic's BaseModel
# https://fastapi.tiangolo.com/tutorial/body/#import-pydantics-basemode
from fastapi import FastAPI
from pydantic import BaseModel # First, you need to import BaseModel from pydantic
# from typing import Union # --> we also can use Union for handeling our dynamic inputs 

'''
you declare your data model as a class that inherits from BaseModel.
when a model attribute has a default value, it is not required, otherwise, it is required.
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

'''
For example, this model above declares a JSON "object" (or Python dict) like:

    {
        "name": "Foo",
        "description": "An optional description",
        "price": 45.2,
        "tax": 3.5
    }

as description and tax are optional (with a default value of None),
this JSON "object" would also be valid:

    {
    "name": "Foo",
    "price": 45.2
    }
'''

# creating fastapi instance
app = FastAPI()


# fuction to create data and accept POST method from user
@app.post("/items/")
async def create_data(item: Item):
    return item