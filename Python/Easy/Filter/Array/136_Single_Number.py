def singleNumber(nums: list[int]) -> int:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for k, v in count.items():
        if v == 1:
            return k



nums = [2, 2, 1]
print(singleNumber(nums))
