def countAsterisks(s: str) -> int:
    ## 1 method

    # if '|' not in s:
    #     return 0
    # result_str = ''.join(s.split('|')[::2])
    # return result_str.count('*')

    ## 2 method

    return sum(result.count('*') for result in s.split('|')[::2])


s = "l|*e*et|c**o|*de|"
# s = "yo|uar|e**|b|e***au|tifu|l"
# s = "iamprogrammer"
print(countAsterisks(s))
