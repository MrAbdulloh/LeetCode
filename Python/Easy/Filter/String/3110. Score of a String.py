def scoreOfString(s: str) -> int:
    ## 1- method
    # add = []
    # total = 0
    # for i in s:
    #     add.append(ord(i))
    #
    # for i in range(len(add) - 1):
    #     total += abs(add[i] - add[i + 1])
    # return total


    total = 0
    for a, b in zip(s, s[1:]):
        print(a,b)
        total += abs(ord(b) - ord(a))
    return total


print(scoreOfString('hello'))