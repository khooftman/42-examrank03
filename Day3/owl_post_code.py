def owl_post_code(code: str, from_base: int, to_base: int) -> str:
    # 1. Valideer of de bases binnen het toegestane bereik vallen
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return "ERROR"
        
    # Zorg dat de code volledig in hoofdletters staat
    code = code.upper()
    if not code:
        return "ERROR"

    # 2. Converteer de broncode naar een decimaal getal (Base 10)
    try:
        # Python's int() kan strings van base 2 t/m 36 omzetten naar base 10.
        # Als er een ongeldig teken in staat voor die base, gooit het een ValueError.
        decimal_value = int(code, from_base)
    except ValueError:
        return "ERROR"

    # 3. Als het getal 0 is, is het resultaat in elke base "0"
    if decimal_value == 0:
        return "0"

    # 4. Converteer het decimale getal naar de doeltarget base (to_base)
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result_chars = []
    
    while decimal_value > 0:
        remainder = decimal_value % to_base
        result_chars.append(digits[remainder])
        decimal_value //= to_base

    # De karakters zijn van achter naar voren berekend, dus we draaien ze om
    return "".join(reversed(result_chars))
