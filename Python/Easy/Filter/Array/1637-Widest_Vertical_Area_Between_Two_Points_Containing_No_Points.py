# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/

def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[0])
    max_width = 0

    for i in range(1, len(points)):
        width = points[i][0] - points[i - 1][0]
        max_width = max(max_width, width)
    return max_width


points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(maxWidthOfVerticalArea(points))
