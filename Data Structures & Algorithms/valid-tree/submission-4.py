class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_map = {}
        for edge in edges:
            print(edge)
            if edge[0] not in adj_map:
                adj_map[edge[0]] = [edge[1]]
            else:
                adj_map[edge[0]].append(edge[1])
            if edge[1] not in adj_map:
                adj_map[edge[1]] = []
            print(adj_map)
        #print(adj_map)
        for node in adj_map:
            visited = set([node])
            to_visit = adj_map[node].copy()
            #print("Node", node, visited, to_visit, adj_map)
            while len(to_visit)!=0:
                temp_node =  to_visit.pop(0)
                #print(node, to_visit, adj_map,visited, temp_node)
                if temp_node in visited:
                    return False
                else:
                    visited.add(temp_node)
                to_visit.extend(adj_map[temp_node])
        connected = set()
        for key, value in adj_map.items():
            if len(connected) == 0:
                connected = set([key]+value)
            elif connected.intersection(set([key]+value)):
                connected = connected.union([key]+value)
        return len(connected) == len(adj_map.keys())
             

        #return True