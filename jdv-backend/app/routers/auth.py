from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import verify_password,create_access_token
from app.schemas.auth import LoginIn,TokenOut
from app.models.user import User
router=APIRouter(prefix='/auth',tags=['auth'])
@router.post('/login',response_model=TokenOut)
def login(body:LoginIn,db:Session=Depends(get_db)):
    u=db.query(User).filter(User.email==body.email).first()
    if not u or not verify_password(body.password,u.password_hash) or not u.ativo:
        raise HTTPException(401,'Credenciais inválidas')
    return TokenOut(access_token=create_access_token(str(u.id),u.role))