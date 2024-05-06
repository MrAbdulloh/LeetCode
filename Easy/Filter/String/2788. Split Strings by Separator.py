def splitWordsBySeparator(words: list[str], separator: str) -> list[str]:
    ## 1- method

    x = f'{separator}'.join(words)
    res = x.split(separator)
    ans = []
    for i in res:
        if i:
            ans.append(i)
    return ans

    ## 2 - method
    #
    # x = ''.join(words).split(separator)
    # ans = []
    # for i in x:
    #     if i:
    #         ans.append(i)
    # return ans

    # return [word for word in ''.join(words).split(separator) if word]


# words = ["one.two.three", "four.five", "six"]
# separator = "."
words = ["$easy$", "$problem$"]
separator = "$"
# words = ["stars.bars.$"]
# separator = "."
print(splitWordsBySeparator(words, separator))
