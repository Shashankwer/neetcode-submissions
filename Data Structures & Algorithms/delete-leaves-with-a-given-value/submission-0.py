# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def deleteNode(node):
            if not node:
                return False
            if not node.left and not node.right:
                if node.val == target:
                    return True
                return False
            left = deleteNode(node.left)
            right = deleteNode(node.right)
            if left:
                node.left = None
            if right:
                node.right = None
            if node.val == target and not node.left and not node.right:
                return True
            return False
        to_delete = deleteNode(root)
        if to_delete:
            return None
        else:
            return root 