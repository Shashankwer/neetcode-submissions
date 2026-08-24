# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        tempNode = TreeNode(val)
        if not root:
            return tempNode
        head,prev, temp = root,root, root
        
        while temp:
            if temp.val < val:
                prev = temp
                temp = temp.right
                if not temp:
                    prev.right = tempNode
                    break
            else:
                prev = temp
                temp = temp.left
                if not temp:
                    prev.left = tempNode
                    break
        return head