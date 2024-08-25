# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root):
    result = []

    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)

    traverse(root)
    return result


root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

root2 = None

root3 = TreeNode(1)

print(postorderTraversal(root1))
print(postorderTraversal(root2))
print(postorderTraversal(root3))
