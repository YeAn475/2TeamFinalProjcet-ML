from fastapi import APIRouter
from app.models.analysis import AnalysisRequest, AnalysisResponse
from app.services.analysis import process_analysis

router = APIRouter(tags=["Analysis"])

@router.post("/analyze", response_model=AnalysisResponse, summary="분석 요청 처리")
async def analyze_data(request: AnalysisRequest):
    # 서비스 호출
    result_message = process_analysis(request.userid)
    
    return {
        "status": "success",
        "message": result_message
    }