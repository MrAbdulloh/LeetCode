# this is method Time Limit Exceeded

# def getCommon(nums1: list[int], nums2: list[int]) -> int:
#     ans = []
#
#     for i in range(len(nums1)):
#         for j in range(len(nums2)):
#             if nums1[i] == nums2[j]:
#                 ans.append(nums1[i])
#
#     if not ans:
#         return -1
#     return ans[0]

def getCommon(nums1: list[int], nums2: list[int]) -> int:
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            return nums1[i]
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return -1


nums1 = [1, 2, 3]
nums2 = [2, 4]

print(getCommon(nums1, nums2))
