def maximumTripletValue(nums: list[int]) -> int:
    n = len(nums)
    max_value = 0

    for j in range(1, n - 1):
        max_left = max(nums[:j])
        max_right = max(nums[j + 1:])

        value = (max_left - nums[j]) * max_right
        max_value = max(max_value, value)

    return max_value if max_value > 0 else 0


nums = [12, 6, 1, 2, 7]
print(maximumTripletValue(nums))
