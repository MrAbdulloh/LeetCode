"""
https://leetcode.com/problems/number-of-changing-keys/description/
"""


def countKeyChanges(s: str) -> int:
    c = 0
    j = 1
    count = 0
    st = s.lower()
    while j < len(s):
        if st[c] != st[j]:
            count += 1
        c += 1
        j += 1
    return count


# s = "aAbBcC"
s = "AaAaAaaA"
print(countKeyChanges(s))
