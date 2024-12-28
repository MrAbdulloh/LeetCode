def arrayPairSum(nums: list[int]) -> int:
    nums.sort()
    ans = 0
    for i in range(0, len(nums), 2):
        ans += nums[i]
    return ans


# return sum(sorted(nums)[::2])


# nums = [1, 4, 3, 2]
nums = [1, 2, 3, 4]
print(arrayPairSum(nums))
