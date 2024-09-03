# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=daily-question&envId=2024-09-03

def getLucky(s: str, k: int) -> int:
    # aa = ''
    # for i in s:
    #     aa += str(ord(i) - ord('a') + 1)
    # # 88
    # result = 0
    # for _ in range(k):
    #     new_sum = 0
    #     for i in aa:
    #         new_sum += int(i)
    #     aa = str(new_sum)
    # return aa

    num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
    for _ in range(k):
        num_str = str(sum(int(digit) for digit in num_str))
    return int(num_str)


s = "iiii"
k = 2
print(getLucky(s, k))
