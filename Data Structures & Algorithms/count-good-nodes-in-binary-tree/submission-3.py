# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def dfs(node, maxVal):
            nonlocal result
            if not node:
                return
            if node.left and node.left.val >= maxVal:
                result += 1
                dfs(node.left, max(maxVal, node.left.val))
            elif node.left:
                dfs(node.left, maxVal)
            if node.right and node.right.val >= maxVal:
                result += 1
                dfs(node.right, max(maxVal, node.right.val))
            elif node.right:
                dfs(node.right, maxVal)
        if not root:
            return result
        result += 1
        dfs(root,root.val)
        return result