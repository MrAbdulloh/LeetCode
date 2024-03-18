"""
https://leetcode.com/problems/split-a-string-in-balanced-strings/
"""


def balancedStringSplit(s: str) -> int:
    r, j = 0, 0
    res = 0
    for i in s:
        if i == 'L': r += 1
        if i == 'R': j += 1
        if r == j: res += 1
    return res


s = "RLRRLLRLRL"
print(balancedStringSplit(s))