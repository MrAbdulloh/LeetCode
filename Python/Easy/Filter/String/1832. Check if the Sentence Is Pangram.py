"""
https://leetcode.com/problems/check-if-the-sentence-is-pangram/
"""


def checkIfPangram(sentence: str) -> bool:
    hash_tb = {}
    for char in sentence:
        hash_tb[char] = hash_tb.get(char, 0) + 1
    if len(hash_tb) == 26: return True
    return False


sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))