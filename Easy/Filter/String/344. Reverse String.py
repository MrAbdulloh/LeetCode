def reverseString(s: list[str]) -> None:
    ## 1 method

    # temp = ''
    # for value in s:
    #     temp += value
    # s.clear()
    # for i in ''.join(reversed(temp)):
    #     s.append(i)

    ## 2 method

    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1



s = ["h", "e", "l", "l", "o"]
print(reverseString(s))
