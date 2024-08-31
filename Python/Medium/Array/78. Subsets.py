from typing import List


def subsets(nums: List[int]) -> List[List[int]]:

    res = [[]]
    for num in nums:
        new_subs = []
        for curr in res:
            new_subs.append(curr + [num])
        res.extend(new_subs)
    return res

    # res = [[]]
    # for num in nums:
    #     new_subs = [curr + [num] for curr in res]
    #     res.extend(new_subs)
    # return res




nums = [1, 2, 3]
print(subsets(nums))
