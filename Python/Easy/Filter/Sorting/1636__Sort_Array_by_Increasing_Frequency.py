from collections import Counter


# def frequencySort(nums: list[int]) -> list[int]:
#     chars = Counter(nums)
#     results = []
#     for i, j in sorted(chars.items(), key=lambda x: (x[1], -x[0])):
#         results.extend([i] * j)
#     return results

def frequencySort(nums: list[int]) -> list[int]:
    chars = Counter(nums)
    return sorted(nums, key=lambda x: (chars[x], -x))

# nums = [1, 1, 2, 2, 2, 3]
nums = [2,3,1,3,2]
# nums = [-1,1,-6,4,5,-6,1,4,1]
print(frequencySort(nums))
