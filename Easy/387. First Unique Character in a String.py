"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""


def first_non_repeating_char(s: str):
    char_counts = dict()
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i
    return -1


s = 'leetcoode'
print(first_non_repeating_char(s))
