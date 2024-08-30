# def numIdenticalPairs(nums: list[int]) -> int:
#     count = 0
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 count += 1
#     return count

def numIdenticalPairs(nums):
    count = {}
    result = 0
    for num in nums:
        if num in count:
            result += count[num]
            count[num] += 1
        else:
            count[num] = 1
    return result


nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))
