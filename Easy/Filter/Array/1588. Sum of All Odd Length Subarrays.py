def sumOddLengthSubarrays(arr: list[int]):
    total_sum = 0
    n = len(arr)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if (j - i + 1) % 2 == 1:
                total_sum += current_sum
    return total_sum


arr1 = [1, 4, 2, 5, 3]
arr2 = [1, 2]
arr3 = [10, 11, 12]
print(sumOddLengthSubarrays(arr1))  # Output: 58
print(sumOddLengthSubarrays(arr2))  # Output: 3
print(sumOddLengthSubarrays(arr3))  # Output: 66
