class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_map = {}
        for edge in edges:
            if edge[0] not in adj_map:
                adj_map[edge[0]] = [edge[1]]
            else:
                adj_map[edge[0]].append(edge[1])
            if edge[1] not in adj_map:
                adj_map[edge[1]] = [edge[0]]
            else:
                adj_map[edge[1]].append(edge[0])
        # perform bfs or dfs to get the connected components in the graph
        visited = set()
        total_components = 0
        for node in adj_map:
            if node not in visited:
                visited.add(node)
                total_components += 1
                temp_nodes = adj_map[node].copy()
                while len(temp_nodes)!=0:
                    tn = temp_nodes.pop(0)
                    if tn not in visited:
                        visited.add(tn)
                        temp_nodes.extend(adj_map[tn])
        if len(visited) == n:
            return total_components
        else:
            return total_components + (n -len(visited))

