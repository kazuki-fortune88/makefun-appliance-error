import os


LINE = "Error E7: your duvet is now a brick. I refuse to open until someone apologises to the drum."


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    path = os.path.join(output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
