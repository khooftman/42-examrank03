def seed_packet_sort(labels: list[str]) -> list[str]:
    def sort_key(label: str):
        vowels = sum(1 for c in label if c.lower() in 'aeiou')
        return (len(label), label.lower(), vowels)

    result = list(labels)
    n = len(result)

    # Stabiele Bubble Sort
    for i in range(n):
        for j in range(n - 1 - i):
            if sort_key(result[j]) > sort_key(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]

    return result
