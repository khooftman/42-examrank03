def hidden_word(secret: str, boards: str) -> bool:
    # Een leeg geheim woord is altijd verborgen
    if not secret:
        return True
        
    # Als het geheime woord langer is dan de schutting, past het nooit
    if len(secret) > len(boards):
        return False

    secret_pointer = 0
    secret_length = len(secret)

    # Loop door alle planken van de schutting heen
    for board in boards:
        # Als de letters exact overeenkomen (hoofdlettergevoelig)
        if board == secret[secret_pointer]:
            secret_pointer += 1
            
        # Zodra we alle letters van het geheime woord hebben gevonden, zijn we klaar
        if secret_pointer == secret_length:
            return True

    # Als de loop stopt en we hebben niet alle letters gevonden, is het False
    return False
