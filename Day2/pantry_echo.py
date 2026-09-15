def echo_chant(label: str) -> bool:
    cleaned = "".join(label.split()).lower()

    if not cleaned:
        return False

    return cleaned == cleaned[::-1]