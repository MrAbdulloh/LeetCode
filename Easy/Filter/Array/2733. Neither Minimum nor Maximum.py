"""
https://leetcode.com/problems/neither-minimum-nor-maximum/description/
"""


def findNonMinOrMax(nums: list[int]) -> int:
    # if len(set(nums)) == 2 or len(set(nums)) == 1:
    #     return -1
    # num = sorted(nums)
    # return num[1]


    unique_nums = set(nums)
    if len(unique_nums) <= 2:
        return -1
    return sorted(unique_nums)[1]


nums = [2,1,3]
print(findNonMinOrMax(nums))
