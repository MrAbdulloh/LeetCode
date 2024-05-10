def countPrefixes(words: list[str], s: str) -> int:


    ## 1 - method

    # count = 0
    # for word in words:
    #     if s.startswith(word):
    #         count += 1
    # return count

    ## 2 - method

    count = 0
    i = 0
    while i < len(words):
        if s.startswith(words[i]):
            count += 1
        i += 1
    return count


words = ["a", "b", "c", "ab", "bc", "abc"]
s = "abc"
# words = ["a","a"]
# s = "aa"
print(countPrefixes(words, s))
