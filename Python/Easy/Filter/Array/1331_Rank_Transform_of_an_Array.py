def arrayRankTransform(arr: list[int]) -> list[int]:
    sorted_arr = sorted(set(arr))
    rank_map = {value: rank + 1 for rank, value in enumerate(sorted_arr)}

    x = [rank_map[value] for value in arr]
    return x


arr = [40, 10, 20, 30]
print(arrayRankTransform(arr))
