from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.delete import DeleteTrackRequest
from app.services.delete import delete_user_track
from app.database import get_db

router = APIRouter(tags=["delete"])

@router.post("/deleted-track")
async def handle_delete_track(request: DeleteTrackRequest, db: Session = Depends(get_db)):
    print(f"삭제 요청 수신: 유저({request.users_id}), 트랙({request.tracks_id})")
    
    success = delete_user_track(db, request)
    
    if not success:
        # 삭제할 데이터가 없어도 분석 로직은 돌아가야 할 수 있으므로 상황에 따라 처리
        raise HTTPException(status_code=404, detail="삭제할 트랙을 찾을 수 없습니다.")
        
    # 여기서 '재분석 함수'를 호출하면 됩니다.
    return {"status": "success", "message": "성공적으로 삭제되었으며 재분석을 시작합니다."}