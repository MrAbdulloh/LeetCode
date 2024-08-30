def heightChecker(heights: list[int]) -> int:
    expected = sorted(heights)
    count_mismatches = 0

    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count_mismatches += 1
    return count_mismatches


heights1 = [1,1,4,2,1,3]
print(heightChecker(heights1))