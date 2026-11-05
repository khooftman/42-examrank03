def echo_chant(label: str) -> bool:
    cleaned = "".join(label.split()).lower()

    if not cleaned:
        return False

    return cleaned == cleaned[::-1]



############################################################## alternative to skip digits

def is_alpha_palindrome(text: str) -> bool:
    cleaned = "".join(char.lower() for char in text if char.isalpha())
    
    if not cleaned:
        return False
    return cleaned == cleaned[::-1]
