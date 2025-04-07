# 📐 Pydantic schema for the state

from pydantic import BaseModel

class FAQState(BaseModel):
    question: str
    answer: str = ""
