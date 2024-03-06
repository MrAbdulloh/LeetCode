def sortPeople(name: list[str], heights: list[int]) -> list[int]:
    result = list(zip(name, heights))
    sorted_result = sorted(result, key=lambda x: x[1], reverse=True)
    sorted_name = [data[0] for data in sorted_result]

    return sorted_name


names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]
print(sortPeople(names, heights))
