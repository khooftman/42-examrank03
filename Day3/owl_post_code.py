def owl_post_code(code: str, from_base: int, to_base: int) -> str:
    # 1. Valideer of de bases binnen het toegestane bereik vallen
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36) or not code:
        return "ERROR"
        

    # 2. Converteer de broncode naar een decimaal getal (Base 10)
        # Python's int() kan strings van base 2 t/m 36 omzetten naar base 10.
        # Als er een ongeldig teken in staat voor die base, gooit het een ValueError.

    try:
        val = int(code, from_base)
    except ValueError:
        return "ERROR"

    # 3. Als het getal 0 is, is het resultaat in elke base "0"


    if val == 0:
        return "0"

    # 4. Converteer het decimale getal naar de doeltarget base (to_base)

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    while val > 0:
        remainder = val % to_base
        res.append(digits[remainder])
        val //= to_base

    # De karakters zijn van achter naar voren berekend, dus we draaien ze om

    return "".join(reversed(res))
