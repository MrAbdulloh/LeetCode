import collections


def containsDuplicate(nums: list[int]) -> bool:
    # count = {}
    # for num in nums:
    #     count[num] = count.get(num, 0) + 1
    #
    # for i in count.values():
    #     if i > 1:
    #         return True
    #     return False

    # list_duplicate = set()
    # for num in nums:
    #     if num in list_duplicate:
    #         return True
    #     list_duplicate.add(num)
    # return False

    cnt = collections.defaultdict(int)
    for num in nums:
        cnt[num] += 1
        if cnt[num] == 2:
            return True
    return False


nums = [1, 2, 4, 3]
print(containsDuplicate(nums))
