import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# .env 파일 로드
load_dotenv()

# 환경 변수에서 DB_URL 가져오기
SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL")

# MariaDB 연결 시 'mariadb+pymysql' 형식이 가끔 문제를 일으키면 
# 'mysql+pymysql'로 바꿔서 인식하게 처리할 수도 있습니다.
if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("mariadb"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("mariadb", "mysql")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()