def countPairs(nums: list[int], target: int) -> int:
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                result += 1
    return result


nums = [-6, 2, 5, -2, -7, -1, 3]
target = -2
print(countPairs(nums, target))
