def maximumNumberOfStringPairs(words: list[str]) -> int:
    ss = set()
    count = 0
    for word in words:
        if word in ss:
            count += 1
        ss.add(word[::-1])
    return count


words = ["cd", "ac", "dc", "ca", "zz"]
print(maximumNumberOfStringPairs(words))
