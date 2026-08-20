class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for flight in flights:
            if flight[0] not in graph:
                graph[flight[0]] = {flight[1]:flight[2]}
            else:
                graph[flight[0]][flight[1]] = flight[2]
        res = min(float("inf"), graph.get(src,{}).get(dst,float("inf")))
        if k == 0:
            return res if res != float("inf") else -1
        to_visit = [[src]]
        visited = set([src])
        while len(to_visit) and k>=0:
            print(to_visit, visited, res, k, graph)
            current = to_visit.pop(0)
            temp = []
            for c in current:
                for d in graph.get(c,[]):
                    cost = graph[c][d]
                    if d == dst:
                        #print(res, cost)
                        res = min(res,cost)
                    else:
                        # add the dst cost to the graph and append to_visit
                        if d not in visited:
                            visited.add(d)
                            for f in graph.get(d, {}):
                                graph[d][f]+= cost
                            temp.append(d)
            to_visit.append(temp)
            k -= 1
        return res if res != float("inf") else -1

                    

