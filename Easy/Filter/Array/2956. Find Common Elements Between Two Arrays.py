def findIntersectionValues(nums1: list[int], nums2: list[int]) -> list[int]:
    total_count1 = 0
    total_count2 = 0
    for i in nums1:
        if i in nums2:
            total_count1 += 1
    for j in nums2:
        if j in nums1:
            total_count2 += 1
    return [total_count1, total_count2]


nums1 = [4, 3, 2, 3, 1]
nums2 = [2, 2, 5, 2, 3, 6]

print(findIntersectionValues(nums1, nums2))
