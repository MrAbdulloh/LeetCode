from collections import defaultdict


def sumPrefixScores(words: list[str]) -> list[int]:
    prefix_count = defaultdict(int)

    for word in words:
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            prefix_count[prefix] += 1

    result = []
    for word in words:
        score = 0
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            score += prefix_count[prefix]
        result.append(score)
    return result


words = ["abc", "ab", "bc", "b"]
print(sumPrefixScores(words))
