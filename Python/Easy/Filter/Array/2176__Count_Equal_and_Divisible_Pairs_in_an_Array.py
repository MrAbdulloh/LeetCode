# 1 - method

# def countPairs(nums: list[int], k: int) -> int:
#     n = len(nums)
#     count = 0
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if nums[i] == nums[j] and (i * j) % k == 0:
#                 count += 1
#     return count
#
#
# nums = [3, 1, 2, 2, 2, 1, 3]
# k = 2
# print(countPairs(nums, k))

from math import gcd
from collections import defaultdict


def countPairs(nums: list[int], k: int) -> int:
    num_to_indices = defaultdict(list)
    count = 0

    for i, num in enumerate(nums):
        for j in num_to_indices[num]:
            if (i * j) % k == 0:
                count += 1
        num_to_indices[num].append(i)
    return count


nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
print(countPairs(nums, k))
