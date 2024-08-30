def smallestEvenMultiple(n: int) -> int:
    # if n % 2 == 0:
    #     return n
    # else:
    #     return n * 2


    return n if n % 2 == 0 else n * 2


n = 6
print(smallestEvenMultiple(n))
