"""
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
"""


def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    ## 1 method

    # s = ''
    # ss = ''
    # for i in range(len(word1)):
    #     s += word1[i]
    # for i in range(len(word2)):
    #     ss += word2[i]
    # return s == ss

    ## 2 method

    return ''.join(word1) == ''.join(word2)


word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]
print(arrayStringsAreEqual(word1, word2))
