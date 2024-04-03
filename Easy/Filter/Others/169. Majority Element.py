def majorityElement(nums: list[int]) -> int:
    cache = {}

    res = 0
    max_count = 0

    for num in nums:
        cache[num] = cache.get(num, 0) + 1
        if cache[num] > max_count:
            max_count = cache[num]
            res = num

    return res


lst = [2, 2, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3]

print(majorityElement(lst))
