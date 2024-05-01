def findDisappearedNumbers(nums: list[int]) -> list[int]:
    N = len(nums)
    seen = [0] * (N + 1)
    for num in nums:
        seen[num] = 1

    ans = []
    for i in range(1, N + 1):
        if seen[i] == 0:
            ans.append(i)
    return ans


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))
