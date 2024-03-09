def sumOfUnique(nums: list[int]) -> int:
    count = {}
    x = 0
    for num in nums:
        count[num] = count.get(num, 0) + 1

    for i, j in count.items():
        if j == 1:
            x += i
    return x


# nums = [1, 2, 3, 2]
# nums = [1,1,1,1,1]
nums = [1,2,3,4,5]
print(sumOfUnique(nums))
