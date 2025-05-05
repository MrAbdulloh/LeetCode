from collections import Counter


def minimumPushes(word: str) -> int:
    frequency = Counter(word)
    sorted_freq = sorted(frequency.values(), reverse=True)
    total_pushes = 0
    for i, count in enumerate(sorted_freq):
        pushes = (i // 8) + 1
        total_pushes += pushes * count
    return total_pushes


word = "aabbccddeeffgghhiiiiii"

print(minimumPushes(word))
