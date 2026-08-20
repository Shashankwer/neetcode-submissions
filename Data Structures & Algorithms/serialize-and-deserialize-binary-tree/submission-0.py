# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []
        nodes = [root]
        level = 1
        while len(nodes) > 0:
            temp_nodes = []
            for node in nodes:
                if node:
                    res.append(str(level)+"|"+str(node.val))
                    temp_nodes.extend([node.left, node.right])
                else:
                    res.append(str(level)+"|"+str(None))
            level += 1
            nodes = None
            nodes = temp_nodes.copy()
        return "#".join(map(str,res)) 
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        nodes = data.split("#")
        level_map = {}
        max_level = 1
        for node in nodes:
            level, value = node.split("|")
            if int(level) not in level_map:
                level_map[int(level)] = [TreeNode(int(value)) if value!='None' else None]
            else:
                level_map[int(level)].append(TreeNode(int(value)) if value!='None' else None)
            max_level = max(max_level, int(level))
        for level in range(1,max_level+1):
            index = 0
            for node in level_map[level]:
                if node and node.val:
                    node.left = level_map[level+1][2*index] 
                    node.right = level_map[level+1][2*index+1]
                    index+=1
                
        return level_map[1][0]
                


