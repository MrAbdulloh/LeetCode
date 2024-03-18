"""
https://leetcode.com/problems/goal-parser-interpretation/description/
"""


def interpret(command: str) -> str:
    ## 1 method

    return command.replace('()', 'o').replace('(al)','al')

    ## 2 method

    # aa = command.replace('()', 'o')
    # ans = ''
    # for i in aa:
    #     if i.isalpha():
    #         ans += i
    # return ans


command = "G()()()()(al)"
print(interpret(command))
