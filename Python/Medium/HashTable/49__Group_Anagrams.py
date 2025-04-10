# https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram = defaultdict(list)
    for str in strs:
        key = ''.join(sorted(str))
        anagram[key].append(str)
    return list(anagram.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
