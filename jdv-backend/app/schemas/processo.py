from pydantic import BaseModel
from enum import Enum

class ProcessoStatus(str, Enum):
    ABERTO = 'ABERTO'
    QUARENTENA_INICIADA = 'QUARENTENA_INICIADA'
    CONCLUIDO = 'CONCLUIDO'


class ProcessoCreate(BaseModel):
    sei_numero: str
    exportador_id: int
    epe_id: int


class ProcessoOut(BaseModel):
    id: int
    sei_numero: str
    status: ProcessoStatus

    class Config:
        from_attributes = True
