"""
https://leetcode.com/problems/jewels-and-stones/description/
"""


def numJewelsInStones(jewels: str, stones: str) -> int:
    # total_count1 = 0
    #
    # for i in stones:
    #     if i in jewels:
    #         total_count1 += 1
    #
    # return len(total_count1)


    return len([i for i in stones if i in jewels])
jewels = "zz"
stones = "ZZZ"
print(numJewelsInStones(jewels, stones))
