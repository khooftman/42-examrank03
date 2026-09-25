def staircase_digits(lock: str) -> int:
    # Als de string leeg is of te kort voor een paar, zijn er 0 stappen
    if len(lock) < 2:
        return 0

    step_count = 0
    # Loop door de string en vergelijk elk karakter met het volgende karakter
    for i in range(len(lock) - 1):
        char1 = lock[i]
        char2 = lock[i + 1]
        # Controleer of beide karakters cijfers zijn
        # Converteer naar integers om mee te rekenen
        if char1.isdigit() and char2.isdigit():
            # Een stap is geldig als het tweede cijfer exact 1 groter is dan het eerste
            # Dit sluit automatisch 9 en 0 uit, want 0 is niet 9 + 1
            if int(char2) == int(char1) + 1:
                step_count += 1

    return step_count
