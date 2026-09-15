def weather_vane_spin(markers: list[int], k: int) -> list[int]:
    # Als de ring leeg is, valt er niets te draaien
    if not markers:
        return []

    n = len(markers)
    
    # Gebruik de modulo (%) om te bepalen hoeveel we écht moeten opschuiven.
    # Als k groter is dan de lengte van de lijst, filtert dit de volledige rondjes eruit.
    effective_k = k % n

    # Als de effectieve k 0 is, blijft de ring exact hetzelfde
    if effective_k == 0:
        return list(markers)

    # Snijd de laatste 'effective_k' elementen af en zet ze vooraan de rest van de lijst
    # Dit bootst een rotatie naar rechts perfect na zonder ingebouwde functies
    return markers[-effective_k:] + markers[:-effective_k]
