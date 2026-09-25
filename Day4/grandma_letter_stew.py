def letter_stew(jar_a: str, jar_b: str) -> bool:
    # Maak alles lowercase en haal spaties weg via een list comprehension
    clean_a = [c for c in jar_a.lower() if c != " "]
    clean_b = [c for c in jar_b.lower() if c != " "]
    
    # Als de gesorteerde lijsten gelijk zijn, is de soep gelijk
    return sorted(clean_a) == sorted(clean_b)
