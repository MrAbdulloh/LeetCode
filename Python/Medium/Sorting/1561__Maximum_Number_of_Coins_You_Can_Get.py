def maxCoins(piles: list[int]) -> int:
    # piles.sort(reverse=True)
    # count = 0
    #
    # while piles:
    #     piles.pop(0)
    #     count += piles.pop(0)
    #     piles.pop(-1)
    # return count
# 2 method
    piles.sort(reverse=True)
    count = 0
    n = len(piles) // 3
    for i in range(n):
        count += piles[i * 2 + 1]
    return count


piles = [2, 4, 5]
# piles = [2, 4, 1, 2, 7, 8]
# piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]
print(maxCoins(piles))
