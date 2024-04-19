def isHappy(n: int) -> bool:
    ## first method

    # currect_number = n
    # number = 0
    # numbers = {}

    # while True:
    #     for i in str(currect_number):
    #         number += int(i) ** 2

    #     if number == 1:
    #         return True

    #     if number in numbers:
    #         return False

    #     numbers[currect_number] = 0
    #     currect_number = number
    #     number = 0

    ## second method

    seed = set()

    while n != 1:
        if n in seed:
            return False
        seed.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return True


n = 19
print(isHappy(n))
