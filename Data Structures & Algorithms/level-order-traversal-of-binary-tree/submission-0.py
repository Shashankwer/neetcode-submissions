# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes_to_expand = [[root]]
        result = []
        while len(nodes_to_expand) > 0:
            nodes = nodes_to_expand.pop(-1)
            temp_nodes = []
            temp_result = []
            for node in nodes:
                temp_result.append(node.val)
                if node.left:
                    temp_nodes.append(node.left)
                if node.right:
                    temp_nodes.append(node.right)
            result.append(temp_result)
            if len(temp_nodes):
                nodes_to_expand.append(temp_nodes)
        return result






        