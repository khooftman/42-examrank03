def scarecrow_whisper(order: str, shift: int) -> str:
    # Definieer het alfabet
    abc = "abcdefghijklmnopqrstuvwxyz"
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    for char in order:
        if char in abc:
            # Zoek de oude positie, tel de shift erbij op, en wrap met % 26
            new_index = (abc.index(char) + shift) % 26
            result.append(abc[new_index])
        elif char in ABC:
            new_index = (ABC.index(char) + shift) % 26
            result.append(ABC[new_index])
        else:
            # Spaties en leestekens direct overnemen
            result.append(char)

    return "".join(result)

#############################################################

def scarecrow_whisper(order: str, shift: int) -> str:
    # Als de instructie leeg is, geven we een lege string terug
    if not order:
        return ""

    result = []

    for char in order:
        # Controleer of het karakter een letter is
        if char.isalpha():
            # Bepaal de ASCII-basiswaarde afhankelijk van hoofd- of kleine letter
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            # 1. Converteer karakter naar een getal tussen 0 en 25 (char - base)
            # 2. Pas de verschuiving toe (+ shift)
            # 3. Gebruik modulo 26 om netjes binnen het alfabet te wrappen (werkt ook voor negatieve shifts)
            # 4. Voeg de basiswaarde weer toe om terug te gaan naar de juiste ASCII-code
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            # Cijfers, spaties en leestekens blijven ongewijzigd
            result.append(char)

    return "".join(result)
