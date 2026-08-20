# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        dfs_parsed = []
        temp_nodes = [root]
        while len(temp_nodes)>0:
            currNode = temp_nodes.pop(0)
            #node_vals = [node.val for node in temp_nodes]
            #print(dfs_parsed, currNode.val, node_vals)
            if currNode.left and currNode.right and currNode.left.val not in dfs_parsed and currNode.right.val not in dfs_parsed:
                temp_nodes = [currNode.left, currNode, currNode.right] + temp_nodes
            elif currNode.left and currNode.left.val not in dfs_parsed:
                temp_nodes = [currNode.left, currNode] + temp_nodes
            elif currNode.right and currNode.right.val not in dfs_parsed:
                if len(dfs_parsed) == k-1:
                    return currNode.val
                else:
                    dfs_parsed.append(currNode.val)
                    temp_nodes = [currNode.right] + temp_nodes
            else :
                if currNode.val not in dfs_parsed:
                    if len(dfs_parsed) == k-1:
                        return currNode.val
                    else:
                        dfs_parsed.append(currNode.val)
                    