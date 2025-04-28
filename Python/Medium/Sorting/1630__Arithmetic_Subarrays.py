def checkArithmeticSubarrays(nums: list[int], l: list[int], r: list[int]) -> list[bool]:
    answer = []
    for i in range(len(l)):
        subarray = nums[l[i]: r[i] + 1]
        subarray.sort()
        is_arithmetic = True
        diff = subarray[1] - subarray[0]
        for j in range(1, len(subarray) - 1):
            if subarray[j + 1] - subarray[j] != diff:
                is_arithmetic = False
                break
        answer.append(is_arithmetic)
    return answer


nums = [4, 6, 5, 9, 3, 7]
l = [0, 0, 2]
r = [2, 3, 5]
print(checkArithmeticSubarrays(nums, l, r))
