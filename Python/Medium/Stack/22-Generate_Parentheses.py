# https://leetcode.com/problems/generate-parentheses/description/

def generateParenthesis(n):
    stack = [('', 0, 0)]
    result = []

    while stack:
        current, openN, closeN = stack.pop()

        if openN == closeN == n:
            result.append(current)
            continue

        if openN < n:
            stack.append((current + '(', openN + 1, closeN))

        if closeN < openN:
            stack.append((current + ')', openN, closeN + 1))

    return result
