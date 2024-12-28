class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        node = self.root
        for digit in str(number):
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
        node.is_end_of_number = True

    def longest_common_prefix(self, number):
        node = self.root
        prefix_length = 0
        for digit in str(number):
            if digit in node.children:
                node = node.children[digit]
                prefix_length += 1
            else:
                break
        return prefix_length


class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        trie = Trie()
        for num in arr1:
            trie.insert(num)
        max_len = 0
        for num in arr2:
            max_len = max(max_len, trie.longest_common_prefix(num))
        return max_len


arr1 = [123, 456]
arr2 = [1234, 457]

solution = Solution()
print(solution.longestCommonPrefix(arr1, arr2))
