"""Write the make.fun entry word to $OUTPUT_DIR/entry.txt.

Entry: FINE — the word you'd delete from the dictionary.
Deleting FINE ends the universal "I'm fine" lie: nobody can ever
say "I'm fine" again, so every "how are you?" has to be honest.
"""

import os

ENTRY = "FINE"


def main() -> None:
    entry = ENTRY
    if not entry or not entry.strip():
        raise ValueError("entry must be non-blank")
    if not 1 <= len(entry) <= 77:
        raise ValueError("entry must be 1-77 chars")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = entry.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    print(f"entry: {entry}")
    print(f"byte length: {len(data)}")


if __name__ == "__main__":
    main()
