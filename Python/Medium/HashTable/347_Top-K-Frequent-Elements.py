# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter


def topKFrequent(nums: list[int], k: int) -> list[int]:
    if len(nums) == 1:
        return [nums[0]]
    counts = Counter(nums)

    most_common_elements = counts.most_common(k)

    result = [item[0] for item in most_common_elements]
    return result


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))
