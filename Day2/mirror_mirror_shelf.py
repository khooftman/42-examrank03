def mirror_shelves(shelves: list[list[int]]) -> list[list[int]]:
    # Gebruik een list comprehension om een nieuwe lijst te bouwen met omgedraaide rijen
    return [row[::-1] for row in shelves]