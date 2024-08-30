"""
https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
"""


def areOccurrencesEqual(s: str) -> bool:
    count = {}
    for i in s:
        count[i] = count.get(i, 0) + 1
    return len(set(count.values())) == 1


# s = "abacbc"
s = "aaabb"
print(areOccurrencesEqual(s))
