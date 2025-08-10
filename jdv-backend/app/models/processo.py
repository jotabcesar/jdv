from sqlalchemy import Column,Integer,String,DateTime,Enum
from app.core.database import Base
import enum
class ProcessoStatus(str,enum.Enum): ABERTO='ABERTO'; QUARENTENA_INICIADA='QUARENTENA_INICIADA'; CONCLUIDO='CONCLUIDO'
class Processo(Base):
    __tablename__='processos'
    id=Column(Integer,primary_key=True)
    sei_numero=Column(String(50),unique=True,nullable=False)
    exportador_id=Column(Integer,nullable=False)
    epe_id=Column(Integer,nullable=False)
    status=Column(Enum(ProcessoStatus),default=ProcessoStatus.ABERTO,nullable=False)
    quarentena_inicio=Column(DateTime)
    quarentena_fim=Column(DateTime)