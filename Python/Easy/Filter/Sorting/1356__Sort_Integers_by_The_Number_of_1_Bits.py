def sortByBits(arr: list[int]) -> list[int]:
    return sorted(arr, key=lambda num: (bin(num).count("1"), num))


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(sortByBits(arr))
