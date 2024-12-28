def truncateSentence(s: str, k: int) -> str:
    # split_string = s.split()
    return ' '.join(s.split()[:k])


s = "Hello how are you Contestant"
k = 4
print(truncateSentence(s, k))
