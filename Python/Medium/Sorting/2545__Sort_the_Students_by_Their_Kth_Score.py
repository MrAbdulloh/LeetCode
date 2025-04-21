def sortTheStudents(score: list[list[int]], k: int) -> list[list[int]]:
    return sorted(score, key=lambda x: x[k], reverse=True)


score = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]]
k = 2
print(sortTheStudents(score, k))
