def deleteGreatestValue(grid: list[list[int]]) -> int:
    for row in grid:
        row.sort()
    answer = 0
    n = len(grid[0])

    for col in range(n):
        max_deleted = max(row.pop() for row in grid)
        answer += max_deleted
    return answer


grid = [[1, 2, 4], [3, 3, 1]]
print(deleteGreatestValue(grid))
