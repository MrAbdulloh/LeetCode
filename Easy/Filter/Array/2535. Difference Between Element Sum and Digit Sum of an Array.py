def differenceOfSum(nums: list[int]) -> int:
    nums_str = str(nums)
    sum_digits = []

    for num in nums_str:
        if num.isalnum():
            sum_digits.append(int(num))
    return sum(nums) - sum(sum_digits)


nums = [1, 15, 6, 3]
print(differenceOfSum(nums))
