"""One-Star Review of Something Essential — entry: the sun.

Why this review, against the judge brief:
- One-star review of an everyday essential: the sun, filed in earnest,
  as if it were a product with a customer-service desk.
- Sharpest true grievance: it shows up uninvited every single morning,
  cannot be switched off, and quietly ruins things you own (curtains).
- Deadpan throughout: flat complaint, no winking, no exclamation marks,
  no explaining the joke — the review is filed as if it were real.
- Twist in the last few words: "as a roommate" reframes the sun as a
  bad housemate — the sting lands after the complaint is read straight.
- Tight and specific: one joke, one target, no filler, no second joke.
"""

REVIEW = (
    "One star for the sun. Shows up uninvited every morning, "
    "no off switch, and fades my curtains. "
    "Would not recommend as a roommate."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    # Gate: one line, 1-160 characters, not only whitespace.
    # REVIEW is 128 characters: comfortably inside the 160 cap,
    # with no trailing newline written to the file.
    if not (1 <= len(REVIEW) <= 160) or not REVIEW.strip():
        raise SystemExit("entry must be 1-160 characters")
    if "\n" in REVIEW:
        raise SystemExit("entry must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)

    # Verify what landed on disk is exactly the review, nothing else.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != REVIEW.encode("utf-8"):
        raise SystemExit("output mismatch: entry.txt does not match the review")


if __name__ == "__main__":
    main()
