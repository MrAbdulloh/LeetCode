def repeatedNTimes(nums: list[int]) -> int:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] >= 2:
            return num

    # for i, j in count.items():
    #     if j >= 2:
    #         return i


nums = [5, 1, 5, 2, 5, 3, 5, 4]
print(repeatedNTimes(nums))
