# https://leetcode.com/problems/largest-number/description/?envType=daily-question&envId=2024-09-18
from functools import cmp_to_key


def largestNumber(nums: list[int]) -> str:
    nums = list(map(str, nums))

    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    nums.sort(key=cmp_to_key(compare))
    result = ''.join(nums)
    return '0' if result[0] == '0' else result


nums = [10, 2]
print(largestNumber(nums))
