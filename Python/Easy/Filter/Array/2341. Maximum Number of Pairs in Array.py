def numberOfPairs(nums: list[int]) -> list[int]:
    count_dict = {}

    for num in nums:
        # if num in count_dict:
        #     count_dict[num] += 1
        # else:
        #     count_dict[num] = 1
        count_dict[num] = count_dict.get(num, 0) + 1
    pairs = 0
    remaining = 0

    for count in count_dict.values():
        pairs += count // 2
        remaining += count % 2

    return [pairs, remaining]


nums1 = [1, 3, 2, 1, 3, 2, 2]
# {1: 2, 3: 2, 2: 3}
print(numberOfPairs(nums1))
