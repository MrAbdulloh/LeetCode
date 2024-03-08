def minOperations(nums: list[int], k: int) -> int:
    # sum_total = 0
    # for num in nums:
    #     if num < k:
    #         sum_total += 1
    # return sum_total
    return len([num for num in nums if num <k])


nums = [1,1,2,4,9]
k = 9
print(minOperations(nums, k))