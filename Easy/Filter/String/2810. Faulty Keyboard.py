def finalString(s: str) -> str:
    while "i" in s:
        index = s.index("i")
        first = s[:index][::-1]
        second = s[index + 1:]

        s = "".join([first, second])
    return s


s = "poiinter"
print(finalString(s))
