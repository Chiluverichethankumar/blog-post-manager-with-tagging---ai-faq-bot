# 🧠 Core logic to fetch the answer from faq_data

from fuzzywuzzy import process
from .data import faq_data
from .schema import FAQState

def get_best_faq_answer(state: FAQState) -> FAQState:
    user_question = state.question
    best_match, score = process.extractOne(user_question, faq_data.keys())

    if score > 70:  # Tune this threshold as needed
        answer = faq_data[best_match]
    else:
        answer = "Sorry, I couldn't find a good match for that question."

    return FAQState(question=user_question, answer=answer)
