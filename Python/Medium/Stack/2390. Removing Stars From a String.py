def removeStars(word: str) -> str:
    stack = []
    for i in word:
        if i == '*':
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)


word = "leet**cod*e"
print(removeStars(word))
