from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode], result: List[int]) -> None:
        if root:
            self.inorder_traversal(root.left, result)
            result.append(root.val)
            self.inorder_traversal(root.right, result)

    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        list1, list2 = [], []
        self.inorder_traversal(root1, list1)
        self.inorder_traversal(root2, list2)

        # Merge two sorted lists
        merged = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1

        while i < len(list1):
            merged.append(list1[i])
            i += 1
        while j < len(list2):
            merged.append(list2[j])
            j += 1

        return merged
