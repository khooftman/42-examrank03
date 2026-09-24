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
        

    
