def seed_packet_sort(labels: list[str]) -> list[str]:
    def vowel_count(s: str) -> int:
        return sum(1 for c in s if c.lower() in 'aeiou')

    def sort_key(label: str):
        return (len(label), label.lower(), vowel_count(label))

    result = list(labels)  # kopie maken, origineel niet aanpassen
    n = len(result)

    for i in range(n):
        for j in range(n - 1 - i):
            # Vergelijk buur j met buur j+1
            if sort_key(result[j]) > sort_key(result[j + 1]):
                # Ze staan verkeerd om -> omwisselen!
                result[j], result[j + 1] = result[j + 1], result[j]

    return result
