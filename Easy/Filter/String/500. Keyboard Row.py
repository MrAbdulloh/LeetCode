def findWords(words: list[str]) -> list[str]:
    first = set('qwertyuiop')
    second = set('asdfghjkl')
    third = set('zxcvbnm')
    result = []
    for word in words:
        w = set(word.lower())
        if w <= first or w <= second or w <= third:
            result.append(word)
    return result


words = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(words))
