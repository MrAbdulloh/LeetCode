"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]

    for string in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
            i += 1

        prefix = prefix[:i]

        if not prefix:
            break

    return prefix


strs1 = ["flower", "flow", "flight"]
print(longest_common_prefix(strs1))
