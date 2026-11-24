#zigzag letters

def zigzag_paint(phrase: str) -> str:
    if not phrase:
        return ""

    result = []
    lower_turn = True

    for char in phrase:
        if char == " ":
            result.append(char)
            lower_turn = True
        elif char.isalpha():
            # Compacte en professionele manier om de case aan te passen
            result.append(char.lower() if lower_turn else char.upper())
            lower_turn = not lower_turn
        else:
            result.append(char)

    return "".join(result)



##############################################################
#Grademe variation
    
    def zigzag_letters(text: str) -> str:
    counter: int = 0
    result: str = ""
    for char in text:
        if char.isalpha():
            if counter % 2 == 0:
                result += char.lower()
            else:
                result += char.upper()
            counter += 1
        else:
            result += char
    return result


---------------
