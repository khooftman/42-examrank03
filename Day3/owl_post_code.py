def owl_post_code(code: str, from_base: int, to_base: int) -> str:
    # 1. Alle controles compact samen op één regel
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36) or not code:
        return "ERROR"
        
    # 2. Omzetten naar decimaal met foutafhandeling
    try:
        val = int(code, from_base)
    except ValueError:
        return "ERROR"
        
    # 3. Randgeval voor nul
    if val == 0: 
        return "0"
    
    # 4. Omzetting met de vertrouwde % en //
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    while val > 0:
        remainder = val % to_base
        res.append(digits[remainder])
        val //= to_base  # Het getal wordt hier kleiner gemaakt voor de volgende ronde
        
    # 5. Omdraaien en samenvoegen tot eindresultaat
    return "".join(reversed(res))

############################################################################################
# alternatief met divmod
def owl_post_code(code: str, from_base: int, to_base: int) -> str:
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return "ERROR"

    code = code.upper()
    if not code:
        return "ERROR"

    try:
        decimal_value = int(code, from_base)
    except ValueError:
        return "ERROR"

    if decimal_value == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []

    while decimal_value > 0:
        decimal_value, remainder = divmod(decimal_value, to_base)
        res.append(digits[remainder])

    return "".join(reversed(res))
        

    
