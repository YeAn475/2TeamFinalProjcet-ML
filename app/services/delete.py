from sqlalchemy.orm import Session
from sqlalchemy import text

def delete_user_track(db: Session, request_data: any):
    # 실제 노래 연결 정보를 담고 있는 playlist_tracks 테이블에서 삭제합니다.
    # DESC 결과에 따라 playlist_id와 track_id를 조건으로 사용합니다.
    query = text("""
        DELETE FROM playlist_tracks 
        WHERE playlist_id = :p_id AND track_id = :t_id
    """)
    
    try:
        result = db.execute(query, {
            "p_id": request_data.playlists_id,
            "t_id": request_data.tracks_id
        })
        db.commit()
        
        # 삭제된 행(row)이 있으면 성공(True) 반환
        if result.rowcount > 0:
            print(f"DB 삭제 성공: 플레이리스트 {request_data.playlists_id}에서 트랙 {request_data.tracks_id} 제거됨")
            return True
        else:
            print(f"삭제 실패: 일치하는 데이터 없음 (p_id: {request_data.playlists_id}, t_id: {request_data.tracks_id})")
            return False
            
    except Exception as e:
        db.rollback()
        print(f"DB 삭제 중 오류 발생: {e}")
        return False