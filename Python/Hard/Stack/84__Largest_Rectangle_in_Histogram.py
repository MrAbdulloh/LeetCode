# https://leetcode.com/problems/largest-rectangle-in-histogram/
def largestRectangleArea(heights: list[int]) -> int:
    stack = []
    max_area = 0
    heights.append(0)

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)

        stack.append(i)

    return max_area


heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))
