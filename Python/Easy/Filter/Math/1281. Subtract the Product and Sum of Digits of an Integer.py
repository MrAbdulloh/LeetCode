def subtractProductAndSum(n: int) -> int:
    ss = list(map(lambda x: int(x), str(n)))
    xx = 1
    for i in ss:
        xx *= i
    xxx = sum(ss)
    return xx - xxx


n = 4421
print(subtractProductAndSum(n))
