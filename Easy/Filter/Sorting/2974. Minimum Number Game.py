def numberGame(nums: list[int]) -> list[int]:
    nums.sort()
    res = []
    for i in range(0, len(nums), 2):
        res.append(nums[i + 1])
        res.append(nums[i])
    return res


nums = [5, 4, 2, 3]
print(numberGame(nums))
