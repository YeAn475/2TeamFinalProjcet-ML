import uvicorn
from fastapi import FastAPI
from app.routers.analysis import router as analysis_router
from app.routers.delete import router as delete_router

app = FastAPI(
    title="PMS 분석 서버",
    description="Spring Boot와 통신하여 데이터를 분석하는 FastAPI 서버입니다.",
    version="1.0.0"
)

# 라우터 등록
app.include_router(analysis_router)
app.include_router(delete_router)

@app.get("/")
def root():
    return {"message": "FastAPI Server is Running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)