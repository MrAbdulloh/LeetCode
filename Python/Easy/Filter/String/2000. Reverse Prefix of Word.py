"""
https://leetcode.com/problems/reverse-prefix-of-word
"""


def reversePrefix(word: str, ch: str) -> str:
    if ch not in word: return word
    index = word.index(ch)
    result = word[:index + 1][::-1] + word[index + 1:]

    return result


word = "abcd"
ch = "z"
print(reversePrefix(word, ch))
