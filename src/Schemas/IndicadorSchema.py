from pydantic import BaseModel, field_validator
from decimal import Decimal
from Utils.Validacionesutilidades import validar_int


class IndicadorCrearSchema(BaseModel):
    nombre_indicador: str
    formula: str
    meta: Decimal
    valor_actual: Decimal = Decimal("0.00")
    id_proyecto: int

    @field_validator("nombre_indicador")
    @classmethod
    def validar_nombre_indicador(cls, v: str) -> str:
        v = v.strip()
        if not (3 <= len(v) <= 45):
            raise ValueError("El nombre del indicador debe tener entre 3 y 45 caracteres.")
        return v

    @field_validator("formula")
    @classmethod
    def validar_formula(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("La fórmula del indicador no puede estar vacía.")
        return v

    @field_validator("meta", "valor_actual")
    @classmethod
    def validar_decimales_positivos(cls, v: Decimal) -> Decimal:
        if v < Decimal("0.00") or v > Decimal("99999999.99"):
            raise ValueError("El valor debe estar entre 0.00 y 99999999.99.")
        return v

    @field_validator("id_proyecto")
    @classmethod
    def validar_ids_positivos(cls, v: int) -> int:
        return validar_int(v, 1, 2147483647, "ID")

class IndicadorRespuestaSchema(BaseModel):
    id_indicador: int
    nombre_indicador: str
    formula: str
    meta: Decimal
    valor_actual: Decimal
    id_proyecto: int

    class Config:
        from_attributes = True