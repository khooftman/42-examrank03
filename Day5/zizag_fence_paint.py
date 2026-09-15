def zigzag_paint(phrase: str) -> str:
    # Als de tekst leeg is, geven we een lege string terug
    if not phrase:
        return ""

    result = []
    # True betekent dat de volgende letter lowercase moet worden, False betekent UPPERCASE
    lower_turn = True

    for char in phrase:
        # Een spatie reset het ritme volledig (de volgende letter begint weer als lowercase)
        if char == " ":
            result.append(char)
            lower_turn = True
        # Als het een letter is, passen we de case aan en wisselen we de beurt
        elif char.isalpha():
            if lower_turn:
                result.append(char.lower())
            else:
                result.append(char.upper())
            # Wissel het ritme om voor de volgende letter
            lower_turn = not lower_turn
        # Cijfers en leestekens veranderen niet en beïnvloeden het ritme niet
        else:
            result.append(char)

    return "".join(result)
