"""Flask API backend for oposiciones test app."""

import json
import os
from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
from temario import parse_temario
from generator import generate_questions
from db import (
    init_db,
    insert_questions,
    get_question_count_per_topic,
    get_total_questions,
    get_exam_questions,
    delete_questions_for_topic,
    get_all_questions,
    get_question_by_id,
    update_question,
    delete_question,
)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-prod")
CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5173"])

TOPICS = parse_temario("temario.md")
TOPICS_BY_NUM = {t.number: t for t in TOPICS}


@app.before_request
def ensure_db():
    init_db()


# ==========================================================================
# API: TOPICS + STATS
# ==========================================================================

@app.route("/api/topics")
def api_topics():
    counts = get_question_count_per_topic()
    total = get_total_questions()
    topics = [
        {
            "number": t.number,
            "title": t.title,
            "group": t.group,
            "count": counts.get(t.number, 0),
        }
        for t in TOPICS
    ]
    return jsonify({"topics": topics, "total": total})


# ==========================================================================
# API: GENERATE
# ==========================================================================

@app.route("/api/generate/<int:topic_num>", methods=["POST"])
def api_generate(topic_num: int):
    topic = TOPICS_BY_NUM.get(topic_num)
    if not topic:
        return jsonify({"error": f"Tema {topic_num} no encontrado"}), 404

    body = request.get_json(silent=True) or {}
    num = int(body.get("num_questions", 2))
    num = min(max(num, 1), 20)

    try:
        questions = generate_questions(topic, num)
        insert_questions(questions)
        return jsonify({"ok": True, "generated": len(questions), "topic": topic.title})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/generate/all", methods=["POST"])
def api_generate_all():
    body = request.get_json(silent=True) or {}
    num_per_topic = int(body.get("num_per_topic", 2))
    num_per_topic = min(max(num_per_topic, 1), 10)
    results = []
    for topic in TOPICS:
        try:
            questions = generate_questions(topic, num_per_topic)
            insert_questions(questions)
            results.append({"topic": topic.number, "generated": len(questions), "ok": True})
        except Exception as e:
            results.append({"topic": topic.number, "error": str(e), "ok": False})
    return jsonify({"results": results})


@app.route("/api/delete/<int:topic_num>", methods=["DELETE"])
def api_delete_topic(topic_num: int):
    delete_questions_for_topic(topic_num)
    return jsonify({"ok": True})


# ==========================================================================
# API: EXAM
# ==========================================================================

@app.route("/api/exam/questions")
def api_exam_questions():
    count = int(request.args.get("count", 80))
    topic_nums_raw = request.args.getlist("topics")
    topic_nums = [int(t) for t in topic_nums_raw] if topic_nums_raw else None
    questions = get_exam_questions(count, topic_nums)
    return jsonify({"questions": questions})


@app.route("/api/exam/score", methods=["POST"])
def api_exam_score():
    body = request.get_json()
    questions = body.get("questions", [])
    answers = body.get("answers", {})  # {str(id): "A"|"B"|"C"|"D"|""}

    correct = wrong = blank = 0
    details = []

    for q in questions:
        qid = str(q["id"])
        selected = answers.get(qid, "")
        is_correct = selected == q["correct"]
        is_blank = selected == ""

        if is_correct:
            correct += 1
        elif is_blank:
            blank += 1
        else:
            wrong += 1

        details.append({
            "question": q["question"],
            "option_a": q["option_a"],
            "option_b": q["option_b"],
            "option_c": q["option_c"],
            "option_d": q["option_d"],
            "correct": q["correct"],
            "selected": selected,
            "is_correct": is_correct,
            "is_blank": is_blank,
            "explanation": q.get("explanation", ""),
        })

    total = len(questions)
    raw_score = 10 * (correct - 0.33 * wrong) / total if total > 0 else 0
    score = max(0, round(raw_score, 2))

    return jsonify({
        "score": score,
        "passed": score >= 5.0,
        "correct": correct,
        "wrong": wrong,
        "blank": blank,
        "total": total,
        "details": details,
    })


# ==========================================================================
# API: QUESTION CRUD
# ==========================================================================

@app.route("/api/questions")
def api_questions():
    questions = get_all_questions()
    return jsonify({"questions": questions})


@app.route("/api/questions", methods=["POST"])
def api_question_add():
    body = request.get_json()
    topic_num = int(body["topic_num"])
    topic = TOPICS_BY_NUM.get(topic_num)
    if not topic:
        return jsonify({"error": "Tema no encontrado"}), 404

    data = {
        "topic_num": topic_num,
        "topic_title": topic.title,
        "group_name": topic.group,
        "question": body["question"].strip(),
        "option_a": body["option_a"].strip(),
        "option_b": body["option_b"].strip(),
        "option_c": body["option_c"].strip(),
        "option_d": body["option_d"].strip(),
        "correct": body["correct"].strip().upper(),
        "explanation": body.get("explanation", "").strip(),
    }
    if data["correct"] not in ("A", "B", "C", "D"):
        return jsonify({"error": "Respuesta correcta debe ser A, B, C o D"}), 400

    insert_questions([data])
    return jsonify({"ok": True})


@app.route("/api/questions/<int:qid>", methods=["PUT"])
def api_question_edit(qid: int):
    body = request.get_json()
    q = get_question_by_id(qid)
    if not q:
        return jsonify({"error": "Pregunta no encontrada"}), 404

    topic_num = int(body["topic_num"])
    topic = TOPICS_BY_NUM.get(topic_num)
    if not topic:
        return jsonify({"error": "Tema no encontrado"}), 404

    data = {
        "topic_num": topic_num,
        "topic_title": topic.title,
        "group_name": topic.group,
        "question": body["question"].strip(),
        "option_a": body["option_a"].strip(),
        "option_b": body["option_b"].strip(),
        "option_c": body["option_c"].strip(),
        "option_d": body["option_d"].strip(),
        "correct": body["correct"].strip().upper(),
        "explanation": body.get("explanation", "").strip(),
    }
    if data["correct"] not in ("A", "B", "C", "D"):
        return jsonify({"error": "Respuesta correcta debe ser A, B, C o D"}), 400

    update_question(qid, data)
    return jsonify({"ok": True})


@app.route("/api/questions/<int:qid>", methods=["DELETE"])
def api_question_delete(qid: int):
    delete_question(qid)
    return jsonify({"ok": True})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, port=port)
