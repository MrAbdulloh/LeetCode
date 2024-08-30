def addDigits(num: int) -> int:

    ## RUNTIME ERROR
    # str_num = str(num)
    # if len(str_num) == 1:
    #     return num
    # ans = sum([int(i) for i in str_num])
    # return addDigits(ans)



    while num >=10:
        num = sum(int(digit) for digit in str(num))
    return num

num = 381242134
print(addDigits(num))
