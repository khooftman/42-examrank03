def scrabble_rack(before: str, after: str) -> bool:
    # Als de lengtes verschillen, kan het nooit een exacte herordening zijn
    if len(before) != len(after):
        return False

    # Maak een dictionary om de frequentie van alle tegels bij te houden
    tile_counts = {}

    # Tel alle tegels op het rekje van 'before'
    for char in before:
        tile_counts[char] = tile_counts.get(char, 0) + 1

    # Trek alle tegels op het rekje van 'after' ervan af
    for char in after:
        # Als een tegel niet in 'before' zat, heeft de ekster valsgespeeld
        if char not in tile_counts:
            return False
        
        tile_counts[char] -= 1
        
        # Als de frequentie onder nul zakt, klopt het aantal niet
        if tile_counts[char] < 0:
            return False

    # Als alle tellingen exact op nul uitkomen, is het een perfecte herordening
    return True
