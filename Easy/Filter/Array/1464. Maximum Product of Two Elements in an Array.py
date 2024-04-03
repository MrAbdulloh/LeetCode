"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
"""


def maxProduct(nums: list[int]) -> int:
    # sorted_nums = sorted(nums)
    # return (sorted_nums[-1] - 1) * (sorted_nums[-2] - 1)

    max1, max2 = float('-inf'), float('-inf')
    for num in nums:
        if num >= max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return (max1 - 1) * (max2 - 1)


nums = [1, 5, 4, 5]
print(maxProduct(nums))
