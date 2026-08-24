# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        head = root
        stack = [root]
        while stack:
            temp_node = stack.pop(0)
            temp_node.left, temp_node.right = temp_node.right, temp_node.left
            if temp_node.left:
                stack.append(temp_node.left)
            if temp_node.right:
                stack.append(temp_node.right)
        return head
            
            