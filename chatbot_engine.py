import datetime
import random
import spacy
import json
import os

# ✅ Load spaCy model safely
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# ✅ Load custom intents (mini brain)
with open("data/intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

def get_intent(user_input):
    """Find best matching intent using semantic similarity"""
    doc = nlp(user_input.lower())
    best_intent = None
    best_score = 0.65  # threshold
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            score = nlp(pattern.lower()).similarity(doc)
            if score > best_score:
                best_intent = intent
                best_score = score
    return best_intent

def get_chatbot_response(user_input):
    intent = get_intent(user_input)
    if intent:
        return random.choice(intent["responses"])

    # Basic rule-based fallback
    if "time" in user_input.lower():
        return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."
    if "date" in user_input.lower():
        return f"Today’s date is {datetime.datetime.now().strftime('%A, %B %d, %Y')}."

    return random.choice([
        "Interesting… tell me more!",
        "Hmm, I’m not sure I got that.",
        "Could you explain that a bit differently?",
        "I’d love to learn more about that!",
    ])
