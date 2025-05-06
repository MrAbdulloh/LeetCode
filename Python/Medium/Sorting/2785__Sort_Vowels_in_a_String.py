# # 1 - method
# def sortVowels(s: str) -> str:
#     result = ''
#     vowels = sorted([c for c in s if c in "aeiouAEIOU"])
#     for i in s:
#         if i in "aeiouAEIOU":
#             result += vowels.pop(0)
#         else:
#             result += i
#     return result

# 2 - method
# def sortVowels(s: str) -> str:
#     vowels = sorted([c for c in s if c in "aeiouAEIOU"])
#     result = list(s)
#     index = 0
#
#     for i in range(len(s)):
#         if s[i] in vowels:
#             result[i] = vowels[index]
#             index += 1
#     return ''.join(result)
#


def sortVowels(s: str) -> str:
    vowels = sorted((c for c in s if c in "aeiouAEIOU"))
    result = list(s)
    vowel_iter = iter(vowels)

    for i, char in enumerate(s):
        if char in "aeiouAEIOU":
            result[i] = next(vowel_iter)
    return "".join(result)


s = "lEetcOde"
print(sortVowels(s))
