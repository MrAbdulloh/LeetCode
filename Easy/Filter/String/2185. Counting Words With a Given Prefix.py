"""
https://leetcode.com/problems/counting-words-with-a-given-prefix/description/
"""


def prefixCount(words: list[str], pref: str) -> int:
    count = 0
    for word in words:
        if word.startswith(pref):
            count += 1
    return count


words = ["pay","attention","practice","attend"]
pref = "at"

print(prefixCount(words, pref))
