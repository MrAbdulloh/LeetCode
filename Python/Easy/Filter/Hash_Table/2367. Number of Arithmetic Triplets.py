def arithmeticTriplets(nums: list[int], diff: int) -> int:
    count = 0
    nums_set = set(nums)
    for num in nums:
        if num + diff in nums_set and num + 2 * diff in nums_set:
            count += 1
    return count


nums = [0, 1, 4, 6, 7, 10]
diff = 3

print(arithmeticTriplets(nums, diff))
