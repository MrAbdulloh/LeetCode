# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/?envType=daily-question&envId=2024-09-12

def countConsistentStrings(allowed: str, words: list[str]) -> int:
    count = 0
    for word in words:
        count += 1
        for letter in word:
            if letter not in allowed:
                count -= 1
                break
    return count


allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
print(countConsistentStrings(allowed, words))
