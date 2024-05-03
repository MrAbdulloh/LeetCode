def addedInteger(nums1: list[int], nums2: list[int]) -> int:
    ## 1 method

    # nums1_set = sorted(nums1)
    # nums2_set = sorted(nums2)
    #
    # return nums2_set[0]-nums1_set[0]

    ## 2 method
    diff_sum = sum(nums2) - sum(nums1)
    return diff_sum // len(nums1)

    ## 3 method Big O O(n)
    nums1_set = sorted(nums1)
    nums2_set = sorted(nums2)
    diff = nums2_set[0] - nums1_set[0]
    for i in range(1, len(nums1_set)):
        if nums2_set[i] - nums1_set[i] != diff:
            return 0

    return diff


nums1 = [2,6,4]
nums2 = [9,7,5]
print(addedInteger(nums1, nums2))
# [2, 4, 6]
# [5, 7, 9]
