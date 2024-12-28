# https://leetcode.com/problems/extra-characters-in-a-string/description/?envType=daily-question&envId=2024-09-23

def minExtraChar(s: str, dictionary: list[str]) -> int:
    n = len(s)
    word_set = set(dictionary)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(i):
            if s[j:i] in word_set:
                dp[i] = min(dp[i], dp[j])
    return dp[n]


s = "leetscode"
dictionary = ["leet", "code", "leetcode"]
print(minExtraChar(s, dictionary))
