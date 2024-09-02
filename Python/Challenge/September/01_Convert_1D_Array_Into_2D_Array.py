# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/
from typing import List


def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    if len(original) != n * m:
        return []
    result = []
    for i in range(m):
        result.append(original[i * n: (i + 1) * n])


nums = [1, 2, 3]

m = 1
n = 3
print(construct2DArray(nums, m, n))
