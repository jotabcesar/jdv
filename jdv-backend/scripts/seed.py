from sqlalchemy.orm import sessionmaker
from app.core.database import engine,Base
from app.core.security import hash_password
from app.models.user import User

def run():
    Base.metadata.create_all(bind=engine)
    S=sessionmaker(bind=engine)();
    def add(email,role):
        if not S.query(User).filter_by(email=email).first():
            S.add(User(email=email,password_hash=hash_password('123'),nome=role,role=role))
    for e,r in [('rt@jdv','RT'),('portaria@jdv','PORTARIA'),('manejo@jdv','CHEFE_MANEJO'),('vet@jdv','VETERINARIO')]: add(e,r)
    S.commit(); S.close()
if __name__=='__main__': run()