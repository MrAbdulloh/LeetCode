from collections import Counter

# 1 - method

# def frequencySort(s: str) -> str:
#     char = {}
#     for i in s:
#         char[i] = char.get(i, 0) + 1
#
#     result = ""
#     for i, j in sorted(char.items(), key=lambda x: x[1], reverse=True):
#         result += j * i
#
#     return result

# 2 method
def frequencySort(s: str) -> str:
    count = Counter(s)
    result = ''.join(char * freq for char, freq in count.most_common())
    return result



s = 'Aabb'
print(frequencySort(s))
