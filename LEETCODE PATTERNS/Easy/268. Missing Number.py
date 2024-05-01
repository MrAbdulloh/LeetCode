def missingNumber(nums: list[int]) -> int:
    N = len(nums)
    seen = [0] * (N + 1)
    for num in nums:
        seen[num] = 1
    for i in range(N):
        if seen[i] == 0:
            return i
    return N

    # for i in range(len(nums)+1):
    #     if i not in nums:
    #         return i


n = [9,6,4,2,3,5,7,0,1]
print(missingNumber(n))
