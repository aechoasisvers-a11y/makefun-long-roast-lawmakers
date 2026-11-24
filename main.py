import os

TEXT = (
    "They passed a 400-page law to govern artificial intelligence, "
    "then adjourned the hearing because nobody in the room could "
    "turn the Word file into a PDF."
)


def main():
    # Self-check (pass 2): the gate is 1-320 characters, UTF-8, not only
    # whitespace, and the brief demands exactly one sentence.
    assert 1 <= len(TEXT) <= 320, f"entry is {len(TEXT)} chars, outside 1-320 gate"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    assert TEXT.strip(), "entry must not be only whitespace"
    assert TEXT.count(".") == 1 and TEXT.endswith("."), "entry must be one sentence"
    assert TEXT.encode("utf-8"), "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Read back and confirm the file on disk is byte-identical to the text.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == TEXT, "written entry.txt does not match the intended text"


if __name__ == "__main__":
    main()
