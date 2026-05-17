"""Question generator: loads from seed_data.py, no external LLM."""

from seed_data import SEED_QUESTIONS
from temario import Topic


def get_questions_for_topic(topic: Topic, limit: int = 20) -> list[dict]:
    """Return seed questions for a given topic, up to limit."""
    qs = [q for q in SEED_QUESTIONS if q["topic_num"] == topic.number]
    return qs[:limit]


def generate_questions(topic: Topic, num_questions: int = 5) -> list[dict]:
    """Generate questions for a topic from seed data.

    Returns a list of dicts ready for db.insert_questions.
    Each dict has: topic_num, topic_title, group_name, question,
    option_a..d, correct, explanation.
    """
    seed = get_questions_for_topic(topic, limit=num_questions)
    valid = []
    for q in seed:
        valid.append({
            "topic_num": topic.number,
            "topic_title": topic.title,
            "group_name": topic.group,
            "question": q["question"],
            "option_a": q["option_a"],
            "option_b": q["option_b"],
            "option_c": q["option_c"],
            "option_d": q["option_d"],
            "correct": q["correct"],
            "explanation": q.get("explanation", ""),
        })
    return valid
