
def clearDigits(s: str) -> str:
    result = ''
    for char in s:
        if char.isdigit():
            if result:
                result = result[0:-1]
            continue
        result += char
    return result


s = 'ag3'
print(clearDigits(s))
