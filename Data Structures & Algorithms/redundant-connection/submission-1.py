class Solution:
    def isCyclic(self, graph, start_node):
        visited = set()
        to_visit = [(start_node,-1)]
        #print(graph)
        while len(to_visit):
            node, prev_node = to_visit.pop(0)
            #print(node, visited)
            if node in visited:
                return True
            else:
                visited.add(node)
                for n in graph.get(node, []):
                    if n != prev_node:
                        to_visit.append((n, node))
        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        res = []
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])
            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])
            for node in graph:
                if self.isCyclic(graph, node):
                    res.extend(edge)
                    graph[edge[0]].remove(edge[1])
                    graph[edge[1]].remove(edge[0])
                    break
        return res
            