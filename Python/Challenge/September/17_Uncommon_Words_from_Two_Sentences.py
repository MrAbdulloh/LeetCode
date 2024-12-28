# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/?envType=daily-question&envId=2024-09-17

from collections import Counter


# big O = O(n *m)
# def uncommonFromSentences(s1: str, s2: str) -> list[str]:
#     s11 = Counter(s1.split())
#     s22 = Counter(s2.split())
#
#     list_s11 = set()
#     for i, v in s11.items():
#         if v == 1:
#             list_s11.add(i)
#     list_s22 = set()
#     for i, v in s22.items():
#         if v == 1:
#             list_s22.add(i)
#     return list(list_s11 ^ list_s22)
#
#
# # s1 = "this apple is sweet"
# # s2 = "this apple is sour"
# # s1 = "apple apple"
# # s2 = "banana"
# s1 = "abcd def abcd xyz"
# s2 = "ijk def ijk"
# print(uncommonFromSentences(s1, s2))


# Big O = O(n)
def uncommonFromSentences(s1: str, s2: str) -> list[str]:
    combined_words = s1.split() + s2.split()
    count = Counter(combined_words)

    return [word for word, freq in count.items() if freq == 1]


# s1 = "this apple is sweet"
# s2 = "this apple is sour"
# s1 = "apple apple"
# s2 = "banana"
s1 = "abcd def abcd xyz"
s2 = "ijk def ijk"
print(uncommonFromSentences(s1, s2))
