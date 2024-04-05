def removeElement(nums: list[int], val: int) -> int:
    k = 0
    for num in nums:
        if num != val:
            nums[k] = num
            k += 1
    return k


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))
