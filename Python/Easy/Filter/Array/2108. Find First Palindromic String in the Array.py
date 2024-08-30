def firstPalindrome(words: list[str]) -> str:
    # s = []
    # for i in range(len(words)):
    #     if words[i] == words[i][::-1]:
    #         s.append(words[i])
    # if not s:
    #     return ''
    # return ''.join(s[0])

    for word in words:
        if word == word[::-1]:
            return word
    return ''

# words = ["abc","car","ada","racecar","cool"]
words = ["def", "ghi"]
print(firstPalindrome(words))
