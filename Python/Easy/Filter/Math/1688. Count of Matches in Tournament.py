def numberOfMatches(n: int) -> int:
    ans = 0
    while n > 1:
        ans += (n // 2)
        # n = divmod(n, 2)
        # n = (n // 2) + (n % 2)
        a, b = divmod(n, 2)
        n = a + b
    return ans


print(numberOfMatches(7))
