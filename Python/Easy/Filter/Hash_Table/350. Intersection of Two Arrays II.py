from collections import Counter


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    # # 1 - method
    # count1 = Counter(nums1)
    # count2 = Counter(nums2)
    #
    # result = []
    #
    # for num in count1:
    #     if num in count2:
    #         result.extend([num] * min(count1[num], count2[num]))
    # return result

    ## 2 - method

    nums1.sort()
    nums2.sort()
    result = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return result


# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))
