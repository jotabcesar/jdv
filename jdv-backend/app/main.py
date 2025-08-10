from fastapi import FastAPI
from app.core.database import Base,engine
Base.metadata.create_all(bind=engine)
from app.routers import auth,processos
app=FastAPI(title='JDV API (mini)')
app.include_router(auth.router)
app.include_router(processos.router)