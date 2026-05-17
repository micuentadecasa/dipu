"""SQLite storage for exam questions."""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "questions.db"


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    """Create tables if they don't exist."""
    conn = get_conn()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS questions (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_num   INTEGER NOT NULL,
            topic_title TEXT    NOT NULL,
            group_name  TEXT    NOT NULL,
            question    TEXT    NOT NULL,
            option_a    TEXT    NOT NULL,
            option_b    TEXT    NOT NULL,
            option_c    TEXT    NOT NULL,
            option_d    TEXT    NOT NULL,
            correct     TEXT    NOT NULL CHECK(correct IN ('A','B','C','D')),
            explanation TEXT    DEFAULT '',
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE INDEX IF NOT EXISTS idx_topic ON questions(topic_num);
    """)
    conn.commit()
    conn.close()


def insert_questions(questions: list[dict]):
    """Insert a batch of questions."""
    conn = get_conn()
    conn.executemany("""
        INSERT INTO questions (topic_num, topic_title, group_name, question,
            option_a, option_b, option_c, option_d, correct, explanation)
        VALUES (:topic_num, :topic_title, :group_name, :question,
            :option_a, :option_b, :option_c, :option_d, :correct, :explanation)
    """, questions)
    conn.commit()
    conn.close()


def get_questions_for_topic(topic_num: int) -> list[dict]:
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM questions WHERE topic_num = ? ORDER BY RANDOM()", (topic_num,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_question_count_per_topic() -> dict[int, int]:
    conn = get_conn()
    rows = conn.execute(
        "SELECT topic_num, COUNT(*) as cnt FROM questions GROUP BY topic_num"
    ).fetchall()
    conn.close()
    return {r["topic_num"]: r["cnt"] for r in rows}


def get_total_questions() -> int:
    conn = get_conn()
    row = conn.execute("SELECT COUNT(*) as cnt FROM questions").fetchone()
    conn.close()
    return row["cnt"]


def get_exam_questions(count: int = 80, topic_nums: list[int] | None = None) -> list[dict]:
    """Get random questions for an exam. If topic_nums is provided, filter by those topics."""
    conn = get_conn()
    if topic_nums:
        placeholders = ",".join("?" * len(topic_nums))
        rows = conn.execute(
            f"SELECT * FROM questions WHERE topic_num IN ({placeholders}) ORDER BY RANDOM() LIMIT ?",
            (*topic_nums, count),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM questions ORDER BY RANDOM() LIMIT ?", (count,)
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def delete_questions_for_topic(topic_num: int):
    conn = get_conn()
    conn.execute("DELETE FROM questions WHERE topic_num = ?", (topic_num,))
    conn.commit()
    conn.close()


def get_question_by_id(qid: int) -> dict | None:
    conn = get_conn()
    row = conn.execute("SELECT * FROM questions WHERE id = ?", (qid,)).fetchone()
    conn.close()
    return dict(row) if row else None


def update_question(qid: int, data: dict):
    conn = get_conn()
    conn.execute("""
        UPDATE questions SET
            topic_num = :topic_num,
            topic_title = :topic_title,
            group_name = :group_name,
            question = :question,
            option_a = :option_a,
            option_b = :option_b,
            option_c = :option_c,
            option_d = :option_d,
            correct = :correct,
            explanation = :explanation
        WHERE id = :id
    """, {**data, "id": qid})
    conn.commit()
    conn.close()


def delete_question(qid: int):
    conn = get_conn()
    conn.execute("DELETE FROM questions WHERE id = ?", (qid,))
    conn.commit()
    conn.close()


def get_all_questions() -> list[dict]:
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM questions ORDER BY topic_num, id"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
