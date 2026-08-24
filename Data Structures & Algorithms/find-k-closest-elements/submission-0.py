class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dist = [(-abs(x-i),-i) for i in arr]
        print(dist)
        max_heap = []
        for val in dist:
            heapq.heappush(max_heap, val)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return sorted([-val[1] for val in max_heap])


