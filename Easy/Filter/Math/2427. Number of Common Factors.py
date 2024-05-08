def commonFactors(a: int, b: int) -> int:
    min_number = min(a, b)
    ans = 0
    for i in range(1, min_number + 1):
        if a % i == 0 and b % i == 0:
            ans += 1
    return ans


a = 12
b = 6
# a = 25
# b = 30
print(commonFactors(a, b))
