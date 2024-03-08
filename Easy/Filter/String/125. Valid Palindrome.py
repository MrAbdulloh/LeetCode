def isPalindrome(s: str) -> bool:
    ss = ''
    for i in s:
        if i.isalnum():
            ss += i.lower()

    return ss == ss[::-1]


# s = "A man, a plan, a canal: Panama"
s = "race a car"
print(isPalindrome(s))
