from collections import Counter


# def canBeEqual(target: list[int], arr: list[int]) -> bool:
#     target.sort()
#     arr.sort()
#     return target == arr


def canBeEqual(target: list[int], arr: list[int]) -> bool:
    return Counter(target) == Counter(arr)

target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]
print(canBeEqual(target, arr))
