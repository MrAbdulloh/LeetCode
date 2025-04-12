from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    magazine_c = Counter(magazine)
    ransom_c = Counter(ransomNote)

    for i, v in ransom_c.items():
        if magazine_c[i] < v:
            return False
    return True


ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote, magazine))
