def minPairSum(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    max_pair_sum = 0

    for i in range(n // 2):
        print(f'{nums[i]}    {nums[n - 1 - i]}')
        pair_sum = nums[i] + nums[n - 1 - i]
        max_pair_sum = max(max_pair_sum, pair_sum)

    # return max_pair_sum


nums = [3, 5, 2, 3]
# nums = [4, 1, 5, 1, 2, 5, 1, 5, 5, 4]
print(minPairSum(nums))
