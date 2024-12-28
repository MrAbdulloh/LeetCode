# https://leetcode.com/problems/shortest-palindrome/description/

def shortestPalindrome(s: str) -> str:
    rev_s = s[::-1]

    combined_s = s + '#' + rev_s

    def compute_kmp_table(s):
        n = len(s)
        kmp = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = kmp[j - 1]
            if s[i] == s[j]:
                j += 1
            kmp[i] = j
        return kmp

    kmp_table = compute_kmp_table(combined_s)

    longest_palindromic_prefix_len = kmp_table[-1]

    non_palindromic_suffix = s[longest_palindromic_prefix_len:]

    return non_palindromic_suffix[::-1] + s


s = "aacecaaa"
print(shortestPalindrome(s))
