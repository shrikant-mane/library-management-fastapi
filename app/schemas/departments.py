from pydantic import BaseModel, EmailStr

# request schema
class CreateDepartment(BaseModel):
    id : int
    name : str
    email : EmailStr
    head_of_department : str


# response schema
class ResponseDepartment(BaseModel):
    id: int
    name: str
    email: EmailStr
    head_of_department: str

    class Config:
        from_attributes = True



