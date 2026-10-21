from fastapi import APIRouter

from backend.app.schemas.learning import ChatRequest, FlashcardRequest, FlashcardSet, FlowchartResult, QuizRequest, QuizSet, TopicRequest
from backend.app.services.learning import chat, flashcards, flowchart, quiz

router = APIRouter(prefix="/api")


@router.get("/health")
def health():
    return {"status": "ok", "service": "luma-learning-api"}


@router.post("/chat")
def tutor(request: ChatRequest):
    return {"reply": chat(request)}


@router.post("/flashcards", response_model=FlashcardSet)
def make_flashcards(request: FlashcardRequest):
    return flashcards(request)


@router.post("/quiz", response_model=QuizSet)
def make_quiz(request: QuizRequest):
    return quiz(request)


@router.post("/flowchart", response_model=FlowchartResult)
def make_flowchart(request: TopicRequest):
    return flowchart(request)
