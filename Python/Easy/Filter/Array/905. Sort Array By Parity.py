def sortArrayByParity(nums: list[int]) -> list[int]:
    return sorted(nums, key=lambda x: x % 2)

#     x = []
#     y = []
#
#     for num in nums:
#         if num % 2 == 0:
#             x.append(num)
#         else:
#             y.append(num)
#     return sum([x, y], [])



nums = [3,1,2,4]

print(sortArrayByParity(nums))
