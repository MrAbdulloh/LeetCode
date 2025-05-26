from collections import Counter


def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
    count = Counter(arr1)
    result = []

    for num in arr2:
        result.extend([num] * count[num])
        del count[num]

    for num in sorted(count.keys()):
        result.extend([num] * count[num])

    return result


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(relativeSortArray(arr1, arr2))
