def restoreString(s: str, indices: list[int]) -> str:
    ans = ''
    for i in range(len(indices)):
        ans += s[indices.index(i)]
    return ans


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
print(restoreString(s, indices))
