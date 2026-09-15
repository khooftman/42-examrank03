def letter_stew(jar_a: str, jar_b: str) -> bool:
    # 1. Maak een hulpfunctie om een string op te schonen naar een letter-frequentie dictionary
    def get_letter_counts(text: str) -> dict[str, int]:
        counts = {}
        for char in text.lower():
            # Negeer spaties (en eventuele andere niet-letter tekens indien gewenst)
            if char != " " and char.isalnum():
                counts[char] = counts.get(char, 0) + 1
        return counts

    # 2. Verkrijg de letter-tellingen voor beide potten
    counts_a = get_letter_counts(jar_a)
    counts_b = get_letter_counts(jar_b)

    # 3. Vergelijk of de dictionaries identiek zijn
    return counts_a == counts_b
