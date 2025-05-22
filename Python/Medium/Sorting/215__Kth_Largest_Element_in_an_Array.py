# class Solution:
#     def partition(self, arr, low, high):
#         pivot = arr[high]
#         i = low - 1
#
#         for j in range(low, high):
#             if arr[j] <= pivot:
#                 i += 1
#                 arr[i], arr[j] = arr[j], arr[i]
#         arr[i + 1], arr[high] = arr[high], arr[i + 1]
#         return i + 1
#
#     def quickSort(self, arr, low, high):
#         if low < high:
#             pivot = self.partition(arr, low, high)
#             self.quickSort(arr, low, pivot - 1)
#             self.quickSort(arr, pivot + 1, high)
#
#     def findKthLargest(self, nums: list[int], k: int) -> int:
#         self.quickSort(nums, 0, len(nums) - 1)
#         return nums[-k]
#
#
# # nums = [3, 2, 1, 5, 6, 4]
# # k = 2
#
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
# s = Solution()
# print(s.findKthLargest(nums, k))

from random import randint


class Solution:
    def quickSort(self, arr, low, high) -> list[int]:
        if low >= high:
            return

        pivot_index = randint(low, high)
        pivot = arr[pivot_index]

        lt = low
        i = low
        gt = high

        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        self.quickSort(arr, low, lt - 1)
        self.quickSort(arr, gt + 1, high)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums[-k]


nums = [3, 2, 1, 5, 6, 4]
k = 2

# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
s = Solution()
print(s.findKthLargest(nums, k))
