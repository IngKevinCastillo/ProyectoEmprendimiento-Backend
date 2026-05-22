from pydantic import BaseModel
from typing import List, Optional

class MesasBaseSchema(BaseModel):
    nombre: str
    cedula_tutor: str
    cedulas_docentes: Optional[List[str]]

class MesasResultadoSchema(BaseModel):
    id: int
    nombre: str
    cedula_tutor: str
    cedulas_docentes: Optional[List[str]]

    class Config:
        from_attributes = True