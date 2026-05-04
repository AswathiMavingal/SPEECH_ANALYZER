from fastapi import FastAPI
# from agent import ContentModerationSystem
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.models.schemas import HateAnalysis
from app.services.crew_manager import ModerationService

app = FastAPI()
moderator = ModerationService()  # Initialize ONCE at startup

origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]


class PostRequest(BaseModel):
    text: str


class PostAnalysisResponse(BaseModel):
    result: HateAnalysis


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,  # Allows cookies and auth headers
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.post("/analyze", response_model=PostAnalysisResponse)
def analyze(request: PostRequest):
    # moderator = ContentModerationSystem()

    print(f"Received text for analysis: {request.text}")
    result = moderator.run_analysis(request.text)
    return {"result": result}
