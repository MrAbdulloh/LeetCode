def sumZero(n: int) -> list[int]:
    result = []

    if n % 2 != 0:
        result.append(0)

    for i in range(1, n // 2 + 1):
        result.append(i)
        result.append(-i)

    return result

print(sumZero(5))