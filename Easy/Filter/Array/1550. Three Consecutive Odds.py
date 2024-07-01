def threeConsecutiveOdds(arr: list[int]) -> bool:

    ## 2 method

    # size = len(arr)
    # for i in range(size - 2):
    #     if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
    #         return True
    # return False

    ## 2 method

    odds = 0
    for num in arr:
        if num % 2 == 1:
            odds += 1
            if odds == 3:
                return True
        else:
            odds = 0
    return False

arr = [1, 2, 3, 4, 5, 7, 9, 11]
print(threeConsecutiveOdds(arr))
