from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(node):
            if node:
                for child in node.children:
                    dfs(child)
                result.append(node.val)

        dfs(root)
        return result
