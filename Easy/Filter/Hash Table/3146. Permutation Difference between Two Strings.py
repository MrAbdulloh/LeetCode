# https://leetcode.com/problems/permutation-difference-between-two-strings/description


def findPermutationDifference(s: str, t: str) -> int:
    # 1- method used sting O(n^2)
    # result = 0
    # for i, v in enumerate(s):
    #     a = t.index(v)
    #     result += abs(i - a)
    # return result

    # 2 - method used HashMap O(n)
    index_map = {char: i for i, char in enumerate(s)}

    total = 0
    for i, char in enumerate(t):
        total += abs(i - index_map[char])

    return total


# s = "abc"
# t = "bac"


s = "abcde"
t = "edbac"
print(findPermutationDifference(s, t))
