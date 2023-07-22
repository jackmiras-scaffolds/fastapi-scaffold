from typing import Optional

from pydantic import BaseModel, EmailStr, Field, constr


class User(BaseModel):
    id: Optional[int]
    email: EmailStr
    password: constr(
        min_length=8,
        max_length=100,
        regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[a-zA-Z\d!@#$%^&*]+$",
    ) = Field(
        description="Password must be at least 8 characters long and contain at least one lowercase letter, one uppercase letter, one digit, and one special character (!@#$%^&*)",
        example="Password123!",
    )
