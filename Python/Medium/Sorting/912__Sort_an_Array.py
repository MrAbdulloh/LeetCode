import random

class Solution:
    def quickSort(self, arr, low, high):
        if low >= high:
            return

        pivot_index = random.randint(low, high)
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

    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

s = Solution()
print(s.sortArray([1, 3, 5, 7]))