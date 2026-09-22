from pydantic import EmailStr, BaseModel

# request schema
class CreateAdmin(BaseModel):
    id : int
    username : str
    first_name : str
    last_name : str
    email : EmailStr
    password : str


class ResponseAdmin(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        from_attributes = True





    """id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    first_mane = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    """