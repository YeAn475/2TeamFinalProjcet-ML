from pydantic import BaseModel

class DeleteTrackRequest(BaseModel):
    users_id: int
    playlists_id: int
    tracks_id: int