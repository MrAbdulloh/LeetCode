def isAcronym(words: list[str], s: str) -> bool:
    first_word = ''
    for word in words:
        first_word += word[0]
    return first_word == s


    # 2 method
    # return ''.join([word[0] for word in words]) == s


words = ["never", "gonna", "give", "up", "on", "you"]
s = "ngguoy"
print(isAcronym(words, s))
