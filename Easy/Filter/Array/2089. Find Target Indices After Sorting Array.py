def targetIndices(nums: list[int], target: int) -> list[int]:

    sorted_nums = sorted(nums)

    ans = []
    for i, v in enumerate(sorted_nums):
        if v == target:
            ans.append(i)
    return ans

    ## 2 method
    # nums.sort()
    # return [i for i in range(len(nums)) if nums[i] == target]

nums = [1, 2, 5, 2, 3,2]
target = 2
print(targetIndices(nums, target))
