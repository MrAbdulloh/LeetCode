def uniqueOccurrences(arr: list[int]) -> bool:
    count = {}

    for num in arr:
        count[num] = count.get(num, 0) + 1

    ans = []
    for i in count.values():
        if i not in ans:
            ans.append(i)
        else:
            return False
    return True


    # count = {}
    #
    # for num in arr:
    #     count[num] = count.get(num, 0) + 1
    #
    # print(count.values())
    # return len(count.values()) == len(set(count.values()))


arr = [1, 2, 2, 1, 1, 3]
# arr = [1, 2]
print(uniqueOccurrences(arr))
