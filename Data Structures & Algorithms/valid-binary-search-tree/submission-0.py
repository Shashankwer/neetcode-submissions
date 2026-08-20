# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        node_list = [(root, float("-inf"), float("inf"))]
        while len(node_list)>0:
            node, left, right = node_list.pop()
            if not (left < node.val < right):
                return False
            if node.left:
                node_list.append((node.left, left, node.val))
            if node.right:
                node_list.append((node.right, node.val, right))
        return True
        

