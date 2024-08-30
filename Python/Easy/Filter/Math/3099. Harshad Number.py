def sumOfTheDigitsOfHarshadNumber(x: int) -> int:
    x_str = str(x)
    a = 0
    for i in x_str:
        a += int(i)
    if x % a == 0:
        return a
    return -1






x = 13
print(sumOfTheDigitsOfHarshadNumber(x))
