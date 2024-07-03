def minDifference(nums: list[int]) -> int:
    n = len(nums)
    if n <= 4:
        return 0
    nums.sort()
    a1 = abs(nums[3] - nums[-1])
    a2 = abs(nums[2] - nums[-2])
    a4 = abs(nums[1] - nums[-3])
    a5 = abs(nums[0] - nums[-4])

    return min(a1, a2, a4, a5)


nums = [6, 6, 0, 1, 1, 4, 6]

print(minDifference(nums))
