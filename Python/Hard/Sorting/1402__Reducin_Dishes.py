def maxSatisfaction(satisfaction: list[int]) -> int:
    ## 1 - method
    # satisfaction.sort()
    #
    # while sum(satisfaction) <= 0:
    #     if len(satisfaction) == 0:
    #         return 0
    #     satisfaction.pop(0)
    #
    # result = []
    # for i, j in enumerate(satisfaction):
    #     result.append((i + 1) * j)
    # return sum(result)

    ## 2 - method

    satisfaction.sort(reverse=True)
    total, prefix_sum = 0, 0

    for dish in satisfaction:
        if prefix_sum + dish >= 0:
            prefix_sum += dish
            total += prefix_sum
        else:
            break
    return total


# satisfaction = [-1, -8, 0, 5, -9]
satisfaction = [4, 3, 2]
# satisfaction = [-1, -4, -5]
print(maxSatisfaction(satisfaction))
