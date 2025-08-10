from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_user,ensure_role
from app.models.processo import Processo,ProcessoStatus
from app.schemas.processo import ProcessoCreate,ProcessoOut
router=APIRouter(prefix='/processos',tags=['processos'])
@router.post('/',response_model=ProcessoOut)
def criar(body:ProcessoCreate,db:Session=Depends(get_db),user=Depends(get_current_user)):
    ensure_role(user,'RT','EPE','ADMIN')
    if db.query(Processo).filter_by(sei_numero=body.sei_numero).first():
        raise HTTPException(400,'SEI já cadastrado')
    p=Processo(sei_numero=body.sei_numero,exportador_id=body.exportador_id,epe_id=body.epe_id)
    db.add(p); db.commit(); db.refresh(p); return p