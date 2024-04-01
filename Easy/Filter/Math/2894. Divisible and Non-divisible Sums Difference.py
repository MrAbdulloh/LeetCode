def differenceOfSums(n: int, m: int) -> int:
    a = []
    b = []
    for i in range(1, n + 1):
        if i % m != 0:
            a.append(i)
        else:
            b.append(i)
    return (sum(a) - sum(b))


n = 10
m = 3
print(differenceOfSums(n, m))
