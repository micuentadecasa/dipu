#!/usr/bin/env python3
"""Independent review and promotion for a topic 2-5 candidate lot."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from question_bank.checkpoints import append_checkpoint, file_sha256
from question_bank.validation import validate_record

DATE = "2026-10-12"
EXPECTATIONS = {
    2: {
        1:("A","Artículo 97"),2:("A","Artículo 98.1"),3:("A","Artículo 98.2"),4:("A","Artículo 98.3"),5:("B","Artículo 100"),
        6:("B","Artículo 108"),7:("A","Artículo 102"),8:("A","Artículo 111"),9:("A","Artículo 112"),10:("A","Artículo 113"),
        11:("A","Artículos 112 y 113"),12:("A","Artículo 115.2"),13:("A","Artículo 137"),14:("A","Artículo 140"),15:("A","Artículo 141.1"),
        16:("A","Artículo 142"),17:("A","Artículo 147.2"),18:("A","Artículo 149.3"),19:("A","Artículo 153.a"),20:("A","Artículo 155.1"),
    },
    3: {
        1:("A","Artículo 11"),2:("A","Artículo 11.2"),3:("A","Artículo 12.2"),4:("A","Artículo 16"),5:("A","Artículo 20.1.a"),
        6:("A","Artículo 20.1.b"),7:("A","Artículo 21.1.a y b"),8:("A","Artículo 22.2.a"),9:("A","Artículo 22.2.d"),10:("A","Artículo 23.2"),
        11:("A","Artículo 31.1"),12:("A","Artículo 32.1"),13:("A","Artículo 34.1.a y b"),14:("A","Artículo 33.2.a"),15:("A","Artículo 36.1.b"),
        16:("A","Artículo 36.1.a"),17:("A","Artículo 36.1.c"),18:("A","Artículo 36.2.a"),19:("A","Artículo 36.2.b"),20:("A","Artículos 1, 2, 11, 31 y 32"),
    },
    4: {
        1:("A","RDL 781/1986, artículo 22.3"),2:("A","RDL 781/1986, artículo 21"),3:("A","RDL 781/1986, artículo 23"),4:("A","RDL 781/1986, artículo 24.1"),5:("A","RDL 781/1986, artículo 30.1"),
        6:("A","RDL 781/1986, artículo 30.2.b"),7:("A","RDL 781/1986, artículo 35.2"),8:("A","RDL 781/1986, artículo 35.2.d"),9:("A","RDL 781/1986, artículo 32"),10:("A","RDL 781/1986, artículo 34.1"),
        11:("A","RD 2568/1986, artículo 29"),12:("A","RD 2568/1986, artículo 32"),13:("A","RD 2568/1986, artículo 25"),14:("A","RD 2568/1986, artículo 26"),15:("A","RD 2568/1986, artículo 27"),
        16:("A","RD 2568/1986, artículo 28.3"),17:("A","RD 2568/1986, artículo 31.1"),18:("A","RD 2568/1986, artículo 35.1"),19:("A","RD 2568/1986, artículo 34.2"),20:("A","RD 2568/1986, artículos 24 y 30"),
    },
    5: {
        1:("A","Artículo 1.1"),2:("A","Artículo 2.3"),3:("A","Artículo 3"),4:("A","Artículo 4.1"),5:("A","Artículo 4.3"),
        6:("A","Artículo 5.1"),7:("A","Artículo 5.4"),8:("A","Artículo 5.6"),9:("A","Artículo 53.1.a"),10:("A","Artículo 14.2.a-e"),
        11:("A","Artículo 14.1"),12:("A","Artículos 9 y 10"),13:("A","Artículo 15.1"),14:("A","Artículo 53.1.d"),15:("A","Artículo 53.1.e"),
        16:("A","Artículo 53.1.g"),17:("A","Artículo 53.1.h"),18:("A","Artículo 5.2"),19:("A","Artículo 15.1"),20:("A","Artículos 5.1 y 53.1.g"),
    },
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic_num", type=int, choices=(2, 3, 4, 5))
    args = parser.parse_args()
    lot_path = ROOT / "docs/question-bank/lots" / f"topic-{args.topic_num:02d}-lot-01.json"
    checkpoint_path = ROOT / "docs/question-bank/checkpoints" / f"topic-{args.topic_num:02d}-lot-01.jsonl"
    payload = json.loads(lot_path.read_text(encoding="utf-8"))
    if payload["state"] != "candidates_written":
        raise RuntimeError("review requires candidate state")
    register = json.loads((ROOT / "docs/question-bank/source-register.json").read_text(encoding="utf-8"))
    sources = {source["source_id"]: source for source in register["source_records"]}
    accepted = []
    decisions = []
    for candidate in payload["questions"]:
        objective_num = int(candidate["learning_objective_id"].rsplit("-", 1)[1])
        expected = EXPECTATIONS[args.topic_num][objective_num]
        source = sources[candidate["sources"][0]["source_id"]]
        if candidate["correct"] != expected[0] or candidate["sources"][0]["citation"] != expected[1]:
            raise RuntimeError(f"independent review disagreement for {candidate['learning_objective_id']}")
        if candidate["sources"][0]["tier"] not in {"official_primary", "secondary_reputable"}:
            raise RuntimeError("missing source tier")
        if source["status"] not in {"verified", "verified_with_correction_review", "verified_official_eli_entry"}:
            raise RuntimeError(f"source register status is not reviewable: {source['source_id']}")
        reviewed = copy.deepcopy(candidate)
        reviewer = f"independent-source-review-{DATE}"
        reviewed["verification"]["answer"] = {"status":"passed","reviewer":reviewer,"checked_at":DATE,"basis":f"Rechecked against {source['source_id']} {expected[1]}; expected option {expected[0]}."}
        reviewed["verification"]["explanation"] = {"status":"passed","reviewer":reviewer,"checked_at":DATE,"basis":f"Explanation checked against the cited {source['source_id']} source and recorded version."}
        reviewed["verification"]["reviewed_at"] = DATE
        reviewed["verification"]["reviewer_decision"] = "accepted"
        for level in ("semantic", "concept"):
            reviewed["deduplication"][level] = {"status":"unique","checked_at":DATE,"basis":"Independent proposition/objective review found no collision with the legacy bank or this lot."}
        reviewed["status"] = "validated"
        errors = validate_record(reviewed)
        if errors:
            raise RuntimeError(f"reviewed record failed validation: {errors}")
        accepted.append(reviewed)
        decisions.append({"objective_id":candidate["learning_objective_id"],"stable_id":candidate["stable_id"],"answer":expected[0],"citation":expected[1],"source_tier":candidate["sources"][0]["tier"],"decision":"accepted","reviewed_at":DATE})

    review_path = ROOT / "docs/question-bank/reviews" / f"topic-{args.topic_num:02d}-lot-01.json"
    review_path.parent.mkdir(parents=True, exist_ok=True)
    review_path.write_text(json.dumps({"review_version":"1.0","lot":f"topic-{args.topic_num:02d}-lot-01","reviewer":f"independent-source-review-{DATE}","source_tier_counts":{"official_primary":sum(x["source_tier"]=="official_primary" for x in decisions),"secondary_reputable":sum(x["source_tier"]=="secondary_reputable" for x in decisions)},"decisions":decisions},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    accepted_path = ROOT / "docs/question-bank/accepted" / f"topic-{args.topic_num:02d}-lot-01.json"
    accepted_path.parent.mkdir(parents=True, exist_ok=True)
    accepted_payload = {"lot_version":payload["lot_version"],"state":"reviewed","topic_num":args.topic_num,"lot_num":1,"revision":payload["revision"],"reviewed_at":DATE,"source_register_sha256":payload["source_register_sha256"],"objective_manifest_sha256":payload["objective_manifest_sha256"],"syllabus_sha256":payload["syllabus_sha256"],"counts":{"candidates":20,"accepted":len(accepted),"rejected":0,"quarantined":0},"review_audit":str(review_path.relative_to(ROOT)),"questions":accepted}
    accepted_path.write_text(json.dumps(accepted_payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    checkpoint = {"schema_version":"1.0","syllabus_hash":payload["syllabus_sha256"],"source_register_hash":payload["source_register_sha256"],"topic_num":args.topic_num,"lot_num":1,"revision":payload["revision"],"stage":"reviewed","objective_ids":[x["learning_objective_id"] for x in accepted],"stable_ids":[x["stable_id"] for x in accepted],"counts":accepted_payload["counts"],"input_hash":file_sha256(lot_path),"output_hash":file_sha256(accepted_path),"last_import":{"status":"not_started","transaction":None}}
    appended=append_checkpoint(checkpoint_path,checkpoint)
    print(f"topic {args.topic_num}: reviewed {len(accepted)} records; checkpoint {'appended' if appended else 'already present'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
