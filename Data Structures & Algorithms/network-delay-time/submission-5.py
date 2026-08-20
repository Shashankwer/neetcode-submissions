class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i:[] for i in range(1,n+1)}
        for edge in times:
            adj_list[edge[0]].append((edge[2], edge[1]))
        cost = {i:float("inf") if i!=k else 0 for i in range(1, n+1)}
        to_visit = adj_list[k]
        visited = [k]
        heapq.heapify(to_visit)
        while len(to_visit)>0:
            c, e = heapq.heappop(to_visit)
            cost[e] = min(cost[e], c)
            if e not in visited:
                visited.append(e)
                for edge in adj_list[e]:
                    heapq.heappush(to_visit,(cost[e]+edge[0],edge[1]))
                    #print(to_visit)
        res = max([c for e,c in cost.items() if e!=k])
        if res != float("inf"):
            return res
        else:
            return -1
            
            
