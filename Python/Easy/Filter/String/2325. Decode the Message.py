def decodeMessage(key: str, message: str) -> str:
    mapping = {' ': ' '}
    i = 0
    res = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for char in key:
        if char not in mapping:
            mapping[char] = letters[i]
            i += 1

    for char in message:
        res += mapping.get(char, char)
    return res


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

print(decodeMessage(key, message))
