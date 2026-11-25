"""Write the make.fun entry word to $OUTPUT_DIR/entry.txt.

Entry: FINE — the word you'd delete from the dictionary.
Deleting FINE ends the universal "I'm fine" lie: nobody can ever
say "I'm fine" again, so every "how are you?" has to be honest.
A one-word guard below keeps the entry exactly one bare word.
"""

import os

ENTRY = "FINE"


def validate_entry(word: str) -> str:
    """Allow only a single whitespace-free word of 1 to 77 characters."""
    if len(word) < 1 or len(word) > 77:
        raise ValueError("entry must be a single word of 1-77 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no spaces inside")
    return word


def main() -> None:
    entry = validate_entry(ENTRY)
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
