def maxProductDifference(nums: list[int]) -> int:
    nums_sort = sorted(nums)
    return (nums_sort[-1] * nums_sort[-2]) - (nums_sort[0] * nums_sort[1])

nums = [4,2,5,9,7,4,8]
print(maxProductDifference(nums))
