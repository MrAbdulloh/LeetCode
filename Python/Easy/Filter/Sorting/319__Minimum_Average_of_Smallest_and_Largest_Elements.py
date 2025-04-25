# 1 - method

# def minimumAverage(nums: list[int]) -> float:
#     average = []
#
#     while nums:
#         max_num = max(nums)
#         min_num = min(nums)
#         nums.remove(max_num)
#         nums.remove(min_num)
#         average.append((max_num + min_num) / 2)
#
#     return min(average)

def minimumAverage(nums: list[int]) -> float:
    nums.sort()
    average = []

    while nums:
        min_num = nums.pop(0)
        max_num = nums.pop(-1)
        average.append((min_num + max_num) / 2)

    return min(average)


nums = [7, 8, 3, 4, 15, 13, 4, 1]
print(minimumAverage(nums))
