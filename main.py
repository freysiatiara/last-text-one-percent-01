"""Last Text at One Percent — entry program.

Writes the dying phone's final text message to the output path and
nothing else. Standard library only.
"""

import os

ENTRY_TEXT = "1% left. confession: I muted you in 2021 and blamed the network. anyway, bye."


def resolve_output_path():
    """Resolve where to write the entry text.

    Precedence: ENTRY_OUTPUT env var, then OUTPUT_DIR /
    MAKEFUN_OUTPUT_DIR, then /output/entry.txt, then a file next to
    this script. Never a bare relative path in the current directory.
    """
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
