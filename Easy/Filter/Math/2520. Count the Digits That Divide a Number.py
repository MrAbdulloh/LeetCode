def countDigits(num: int) -> int:
    ans = 0
    num_str = str(num)
    for i in num_str:
        if num % int(i) == 0:
            ans += 1
    return ans


print(countDigits(2112))
