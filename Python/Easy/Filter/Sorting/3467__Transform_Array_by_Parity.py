# https://leetcode.com/problems/transform-array-by-parity/description/

def transformArray(nums: list[int]) -> list[int]:
    # result = []
    # for num in nums:
    #     if num % 2 == 0:
    #         result.append(0)
    #     else:
    #         result.append(1)
    # return sorted(result)

    return sorted([0 if num % 2 == 0 else 1 for num in nums])


# nums = [4, 3, 2, 1]
nums = [1, 5, 1, 4, 2]
print(transformArray(nums))
