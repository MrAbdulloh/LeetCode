"""
https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
"""


def numOfStrings(patterns: list[str], word: str) -> int:
    count = 0
    for pattern in patterns:
        if pattern in word:
            count += 1
    return count

    ## 2 method
    # return sum(x in word for x in patterns)


patterns = ["a", "a", "a"]
word = "ab"
print(numOfStrings(patterns, word))
