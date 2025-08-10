import os
class Settings:
    DATABASE_URL=os.getenv('DATABASE_URL','sqlite:///./jdv.db')
    JWT_SECRET=os.getenv('JWT_SECRET','CHANGE_ME')
    JWT_ALGO=os.getenv('JWT_ALGO','HS256')
    ACCESS_MIN=int(os.getenv('ACCESS_MIN',30))
    REFRESH_DAYS=int(os.getenv('REFRESH_DAYS',7))
    UPLOAD_DIR=os.getenv('UPLOAD_DIR','uploads')
settings=Settings()