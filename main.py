# FastAPI 설정 메인
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI 애플리케이션이 실행 중입니다"}
