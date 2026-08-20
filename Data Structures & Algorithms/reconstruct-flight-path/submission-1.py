class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adjacency list
        graph = {}
        for ticket in sorted(tickets)[::-1]:
            if ticket[0] not in graph:
                graph[ticket[0]] = [ticket[1]]
            else:
                graph[ticket[0]].append(ticket[1])
        stack = ["JFK"]
        paths = []
        while stack:
            u = stack[-1]
            if graph.get(u, None):
                v = graph[u].pop()
                stack.append(v)
            else:
                paths.append(stack.pop())
        return paths[::-1]

