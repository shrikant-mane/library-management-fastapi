from pydantic import BaseModel

# request schema
class UserCreate(BaseModel):
    id : int
    username : str
    first_name : str
    last_name : str
    department_name : str
    email : str
    password : str