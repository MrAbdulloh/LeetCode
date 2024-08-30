def theMaximumAchievableX(num: int, t: int) -> int:
    ## 1 -method

    return num + t + t

    ## 2 method

    # if t == 0:
    #     return num
    # return num + min(t, num) + min(t, num - 1)


print(theMaximumAchievableX(5, 3))
