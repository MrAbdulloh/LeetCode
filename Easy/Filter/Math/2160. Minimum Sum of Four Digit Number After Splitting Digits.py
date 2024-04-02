def minimumSum(num: int) -> int:
    a = sorted(str(num))
    return int(a[0] + a[2]) + int(a[1] + a[3])

num = 2932
print(minimumSum(num))
