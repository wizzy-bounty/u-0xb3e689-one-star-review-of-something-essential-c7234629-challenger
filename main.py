import os

_PARTS = (
    "Breathing worked fine on its own for years.",
    "Then I noticed it, and now it is my job.",
)
TEXT = " ".join(_PARTS)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
