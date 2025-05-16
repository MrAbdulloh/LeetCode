from collections import Counter


def minimumIndex(nums: list[int]) -> int:
    n = len(nums)
    freq = Counter(nums)
    dominant = max(freq, key=freq.get)

    count_left = 0
    count_total = freq[dominant]

    for i in range(n - 1):
        if nums[i] == dominant:
            count_left += 1
        if count_left * 2 > (i + 1) and (count_total - count_left) * 2 > (n - i - 1):
            return i
    return -1


nums = [1, 2, 2, 2]
print(minimumIndex(nums))
