from collections import Counter, defaultdict


def mergeSimilarItems(items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
    value_weight_map = defaultdict(int)

    for value, weight in items1:
        value_weight_map[value] += weight

    for value, weight in items2:
        value_weight_map[value] += weight

    return [[value, weight] for value, weight in sorted(value_weight_map.items())]



items1 = [[1, 1], [4, 5], [3, 8]]
items2 = [[3, 1], [1, 5]]
print(mergeSimilarItems(items1, items2))
