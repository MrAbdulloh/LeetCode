"""
https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/
"""


def maximizeSum(nums: list[int], k: int) -> int:
    end_num = max(nums)
    return sum(i for i in range(end_num, end_num + k))


nums = [1, 2, 3, 4, 5]
k = 3
print(maximizeSum(nums, k))
