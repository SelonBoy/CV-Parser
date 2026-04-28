# models/schema.py
from pydantic import BaseModel
from typing import List, Optional

class Experience(BaseModel):
    posisi: str
    start: str
    end: str
    description: Optional[str] = ""

class Education(BaseModel):
    degree: str
    univ: str
    start: str
    end: str
    field: str

class Skills(BaseModel):
    softskills: List[str] = []
    hardskills: List[str] = []

class CVSchema(BaseModel):
    nama: str
    experience: List[Experience] = []
    education: List[Education] = []
    skills: Skills