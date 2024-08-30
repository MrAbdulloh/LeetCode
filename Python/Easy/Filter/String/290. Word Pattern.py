def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(words) != len(pattern):
        return False
    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            if word in word_to_char:
                return False
            char_to_word[char] = word
            word_to_char[word] = char
    return True


pattern = "abba"
s = "dog cat cat dog"
# pattern = "aba"
# s = "cat cat cat dog"
print(wordPattern(pattern, s))
