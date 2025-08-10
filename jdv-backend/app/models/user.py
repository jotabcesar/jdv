from sqlalchemy import Column,Integer,String,Boolean
from app.core.database import Base
class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    email=Column(String(160),unique=True,nullable=False)
    password_hash=Column(String(200),nullable=False)
    nome=Column(String(160),nullable=False)
    role=Column(String(40),nullable=False)
    ativo=Column(Boolean,default=True)