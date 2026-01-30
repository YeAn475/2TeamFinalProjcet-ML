from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    userid: str

class AnalysisResponse(BaseModel):
    status: str
    message: str