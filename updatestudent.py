from pydantic import BaseModel 
from typing import Optional

class UpdateStudent(BaseModel):
    name: Optional[str] 
    course: Optional[str] = None
    age: Optional[int] = None
    #name : Optional[str] = None
    #age : Optional[int] = None
    #course : Optional[str] = None

