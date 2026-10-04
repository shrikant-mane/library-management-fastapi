from pydantic import BaseModel, Field, ConfigDict

class BookCreate(BaseModel):

    name: str = Field(
        min_length=1,
        max_length=255
    )

    author: str = Field(
        min_length=1,
        max_length=255
    )

    isbn: str = Field(
        min_length=1,
        max_length=50
    )

    department_id: int

    available_copy: int = Field(
        ge=0
    )

    total_copy: int = Field(
        gt=0
    )


class BookUpdate(BaseModel):

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=255
    )

    author: str | None = Field(
        default=None,
        min_length=1,
        max_length=255
    )

    isbn: str | None = Field(
        default=None,
        min_length=1,
        max_length=50
    )

    department_id: int | None = None

    available_copy: int | None = Field(
        default=None,
        ge=0
    )

    total_copy: int | None = Field(
        default=None,
        gt=0
    )


class BookResponse(BaseModel):

    id: int
    name: str
    author: str
    isbn: str
    department_id: int
    available_copy: int
    total_copy: int

    model_config = ConfigDict(
        from_attributes=True
    )


