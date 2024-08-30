from collections import Counter


def countWords(words1: list[str], words2: list[str]) -> int:
    ## 1 method (hash set)

    # set1 = set()
    # for word in words1:
    #     if words1.count(word) == 1:
    #         set1.add(word)
    #
    # set2 = set()
    # for word in words2:
    #     if words2.count(word) == 1:
    #         set2.add(word)
    # return len(set1 & set2)

    ## 2 method (hash set)

    count1 = Counter(words1)
    count2 = Counter(words2)

    set1 = set()
    for k_count1, v_count2, in count1.items():
        if v_count2 == 1:
            set1.add(k_count1)

    set2 = set()
    for k_count2, v_count2, in count2.items():
        if v_count2 == 1:
            set2.add(k_count2)
    return len(set1 & set2)

    ## 3 method  (hash table)

    # counter1 = Counter(words1)
    # counter2 = Counter(words2)
    #
    # count = 0
    # for word, freq in counter1.items():
    #     if freq == 1 and counter2.get(word, 0) == 1:
    #         count += 1
    #
    # for word, freq in counter2.items():
    #     if freq == 1 and counter1.get(word, 0) == 1:
    #         count += 1
    #
    # return count


# words1 = ["b", "bb", "bbb"]
# words2 = ["a", "aa", "aaa"]

words1 = ["leetcode", "is", "amazing", "as", "is"]
words2 = ["amazing", "leetcode", "is"]

# words1 = ["a", "ab"]
# words2 = ["a", "a", "a", "ab"]

print(countWords(words1, words2))
