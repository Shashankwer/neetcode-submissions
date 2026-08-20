# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        bfsNodes = [(0,root)]
        level = 0
        while len(bfsNodes)>0:
            temp_nodes = []
            while len(bfsNodes)>0:
                temp_node = bfsNodes.pop(0)
                if temp_node[0] == level:
                    temp_nodes.append(temp_node)
                else:
                    bfsNodes.insert(0, temp_node)
                    break
            for index in range(len(temp_nodes)-1, -1, -1):
                if temp_nodes[index]:
                    #print(temp_nodes[index])
                    result.append(temp_nodes[index][1].val)  # append the value to the result
                    break
            level+=1
            while len(temp_nodes):
                node = temp_nodes.pop(0)
                if node:
                    node = node[1]
                    if node.left and node.right:
                        bfsNodes.extend([(level,node.left), (level,node.right)])
                    elif node.left:
                        bfsNodes.append((level,node.left))
                    elif node.right:
                        bfsNodes.append((level,node.right))    
            #print(len(bfsNodes))
        return result

        