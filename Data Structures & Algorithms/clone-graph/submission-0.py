"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        else:
            node_map = {}
            # dfs map 
            to_visit = []
            visited = []
            root = Node(node.val)
            node_map[node] = root
            for n in node.neighbors:
                temp_node = Node(n.val)
                if n not in node_map:
                    node_map[n] = temp_node
                node_map[node].neighbors.append(temp_node)
                to_visit.append(n)
            visited.append(node)
            while len(to_visit)>0:
                n = to_visit.pop(0)
                if n in visited:
                    continue
                temp_node = node_map.get(n, None)
                if not temp_node:
                    node_map[n] = Node(n.val)
                for neigh in n.neighbors:
                    tn = node_map.get(neigh)
                    if not tn:
                        tn = Node(neigh.val)
                        node_map[neigh] = tn
                    node_map[n].neighbors.append(tn)
                    to_visit.append(neigh)
                visited.append(n)
            return node_map[node]

                    
         

            