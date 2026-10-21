from typing import Literal

from pydantic import BaseModel, Field


class LearnerPreferences(BaseModel):
    name: str = Field(default="", max_length=60)
    level: Literal["beginner", "intermediate", "advanced"] = "beginner"
    learning_goals: list[str] = Field(default_factory=list, max_length=8)
    subjects_of_interest: list[str] = Field(default_factory=list, max_length=8)
    existing_knowledge: list[str] = Field(default_factory=list, max_length=8)
    preferred_learning_style: list[str] = Field(default_factory=list, max_length=8)
    preferred_examples: list[str] = Field(default_factory=list, max_length=8)
    challenging_topics: list[str] = Field(default_factory=list, max_length=8)
    communication_preferences: list[str] = Field(default_factory=list, max_length=8)


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(min_length=1, max_length=6000)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    history: list[ChatMessage] = Field(default_factory=list, max_length=24)
    preferences: LearnerPreferences = Field(default_factory=LearnerPreferences)


class TopicRequest(BaseModel):
    topic: str = Field(min_length=2, max_length=240)
    context: str = Field(default="", max_length=6000)
    preferences: LearnerPreferences = Field(default_factory=LearnerPreferences)


class FlashcardRequest(TopicRequest):
    count: int = Field(default=8, ge=3, le=20)


class QuizRequest(TopicRequest):
    count: int = Field(default=5, ge=3, le=12)


class Flashcard(BaseModel):
    front: str
    back: str
    topic: str


class FlashcardSet(BaseModel):
    title: str
    cards: list[Flashcard] = Field(min_length=3, max_length=20)


class QuizQuestion(BaseModel):
    question: str
    options: list[str] = Field(min_length=4, max_length=4)
    answer_index: int = Field(ge=0, le=3)
    explanation: str


class QuizSet(BaseModel):
    title: str
    questions: list[QuizQuestion] = Field(min_length=3, max_length=12)


class FlowchartResult(BaseModel):
    title: str
    mermaid: str
    summary: str
