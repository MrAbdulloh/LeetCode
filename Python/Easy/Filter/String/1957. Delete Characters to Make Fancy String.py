def makeFancyString(s: str) -> str:
    result = ''
    count = 0

    for i in range(0, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            count = 1

        if count < 3:
            result += s[i]

    return result


s = "leeetcode"
# s = "aaabaaaa"
# s = "aab"
print(makeFancyString(s))
