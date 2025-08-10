from datetime import datetime,timedelta
from jose import jwt,JWTError
from passlib.hash import bcrypt
from fastapi import HTTPException,status,Depends
from fastapi.security import OAuth2PasswordBearer
from .config import settings
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/auth/login')

def hash_password(p): return bcrypt.hash(p)

def verify_password(p,h): return bcrypt.verify(p,h)

def create_access_token(sub,role):
    exp=datetime.utcnow()+timedelta(minutes=settings.ACCESS_MIN)
    return jwt.encode({'sub':sub,'role':role,'exp':exp},settings.JWT_SECRET,algorithm=settings.JWT_ALGO)

def decode_token(t):
    try:
        return jwt.decode(t,settings.JWT_SECRET,algorithms=[settings.JWT_ALGO])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Token inválido')

def get_current_user(token: str = Depends(oauth2_scheme)):
    p=decode_token(token); return {'id':int(p['sub']),'role':p.get('role','')}

def ensure_role(user,*roles):
    if user is None or user.get('role') not in roles: raise HTTPException(403,detail='Permissão negada')