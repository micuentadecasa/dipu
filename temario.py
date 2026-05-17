"""Parse temario.md into structured topics."""

import re
from dataclasses import dataclass


@dataclass
class Topic:
    number: int
    title: str
    group: str
    raw: str


def parse_temario(path: str = "temario.md") -> list[Topic]:
    """Extract topics from temario.md, returning a list of Topic objects."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    topics: list[Topic] = []
    current_group = "Temario genérico"

    # Track group headers
    group_patterns = [
        (r"^Temario genérico", "Temario genérico"),
        (r"^Temario específico", "Temario específico"),
        (r"^Grupo seguridad", "Grupo seguridad"),
        (r"^Grupo base de datos", "Grupo base de datos"),
        (r"^Grupo desarrollo aplicaciones", "Grupo desarrollo aplicaciones"),
        (r"^Subgrupo net Core", "Subgrupo .NET Core y MVC"),
        (r"^Subgrupo Blazor", "Subgrupo Blazor"),
        (r"^Subgrupo control de versiones", "Subgrupo Git"),
        (r"^Grupo administración electrónica", "Grupo administración electrónica"),
    ]

    # Match topic lines like "Tema 1.– ..." or "Tema 10.– ..."
    topic_re = re.compile(r"^Tema\s+(\d+)\.\s*[–-]\s*(.+)$", re.MULTILINE)

    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Check for group header
        for pattern, group_name in group_patterns:
            if re.match(pattern, line):
                current_group = group_name
                break

        # Check for topic
        m = topic_re.match(line)
        if m:
            num = int(m.group(1))
            title = m.group(2).strip()
            # Gather multi-line topic text (continuations that don't start with "Tema" or "Grupo/Subgrupo")
            raw_lines = [line]
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if not next_line:
                    i += 1
                    continue
                if topic_re.match(next_line):
                    break
                if any(re.match(p, next_line) for p, _ in group_patterns):
                    break
                # Skip page markers and section headers
                if re.match(r"^(Número|Página|Viernes|Sección)", next_line):
                    i += 1
                    continue
                raw_lines.append(next_line)
                i += 1
            raw = " ".join(raw_lines)
            topics.append(Topic(number=num, title=title, group=current_group, raw=raw))
            continue
        i += 1

    return topics


def get_topics_summary(topics: list[Topic]) -> str:
    """Return a compact summary for display."""
    lines = []
    current_group = None
    for t in topics:
        if t.group != current_group:
            current_group = t.group
            lines.append(f"\n== {current_group} ==")
        lines.append(f"  {t.number:2d}. {t.title}")
    return "\n".join(lines)


if __name__ == "__main__":
    topics = parse_temario()
    print(f"Found {len(topics)} topics")
    print(get_topics_summary(topics))
