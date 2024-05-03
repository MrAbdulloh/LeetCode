def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    lowest_price = prices[0]
    for price in prices:
        if price < lowest_price:
            lowest_price = price
        max_profit = max(max_profit, price - lowest_price)
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
