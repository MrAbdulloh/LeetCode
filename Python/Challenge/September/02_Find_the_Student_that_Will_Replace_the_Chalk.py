# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/?envType=daily-question&envId=2024-09-02
from typing import List


def chalkReplacer(chalk: List[int], k: int) -> int:
    total_chalk = sum(chalk)
    # k = k % total_chalk
    k %= total_chalk
    for i, c in enumerate(chalk):
        if k < c:
            return i
        k -= c


# chalk = [5, 1, 5]
# k = 22

chalk = [3, 4, 1, 2]
k = 25
print(chalkReplacer(chalk, k))
