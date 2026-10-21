from functools import lru_cache

from fastapi import HTTPException
from langchain_core.messages import BaseMessage
from langchain_groq import ChatGroq

from backend.app.core.config import get_settings


@lru_cache
def get_model() -> ChatGroq:
    settings = get_settings()
    if not settings.groq_api_key:
        raise HTTPException(status_code=503, detail="Set GROQ_API_KEY in the project .env file to enable AI features.")
    return ChatGroq(model=settings.llm_model, api_key=settings.groq_api_key, temperature=0.35)


def invoke(messages: list[BaseMessage], schema=None):
    try:
        model = get_model()
        result = model.with_structured_output(schema).invoke(messages) if schema else model.invoke(messages)
        return result if schema else str(result.content)
    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(status_code=502, detail="The AI service could not complete this request. Check your model settings and try again.") from error
