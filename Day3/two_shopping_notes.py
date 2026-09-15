def shared_letters(note_a: str, note_b: str) -> str:
    set_b = set(note_b)
    seen = set()
    result = []
    
    for char in note_a:
        if char in set_b and char not in seen:
            seen.add(char)
            result.append(char)
            
    return "".join(result)
