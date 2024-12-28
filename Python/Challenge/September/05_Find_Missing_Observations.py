from typing import List


def missingRolls(rolls: List[int], mean: int, n: int) -> List[int]:
    m = len(rolls)
    total_sum = mean * (n + m)
    current_sum = sum(rolls)
    missing_sum = total_sum - current_sum

    if missing_sum < n or missing_sum > 6 * n:
        return []

    result = [missing_sum // n] * n
    remainder = missing_sum % n

    for i in range(remainder):
        result[i] += 1

    return result


# rolls = [3, 2, 4, 3]
# mean = 4
# n = 2

rolls = [1, 5, 6]
mean = 3
n = 4
print(missingRolls(rolls, mean, n))
