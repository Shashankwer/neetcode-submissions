class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_element = {}
        result = []
        for key in nums:
            bucket_element[key] = bucket_element.get(key, 0)+1
        heap = []
        for num in bucket_element.keys():
            heapq.heappush(heap, (bucket_element[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res