def write_file(file_name: str, mode: str, content: str) -> None:
    with open(file_name, mode, encoding="utf8") as f:
        if mode == "a" | "w":
            f.write(content)
        else:
            f.read()