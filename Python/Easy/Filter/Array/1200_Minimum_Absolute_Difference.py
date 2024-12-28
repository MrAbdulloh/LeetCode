"""
https://leetcode.com/problems/minimum-absolute-difference/description/
"""


def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
    arr.sort()
    min_diff = float('inf')
    for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i - 1])

    ans = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == min_diff:
            ans.append([arr[i - 1], arr[i]])

    return ans


# def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
#     ans = []
#     sorted_arr = sorted(arr)
#     min_diff = sorted_arr[0] - sorted_arr[1]
#
#     for i in range(1, len(sorted_arr)):
#         if sorted_arr[i - 1] - sorted_arr[i] == min_diff:
#             ans.append([sorted_arr[i - 1], sorted_arr[i]])
#     return ans


arr = [4, 2, 1, 3]
# arr = [40,11,26,27,-20]
print(minimumAbsDifference(arr))
# minimumAbsDifference(arr)
