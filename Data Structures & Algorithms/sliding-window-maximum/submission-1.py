class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_heap = [(-nums[i],i) for i in range(k)]
        heapq.heapify(max_heap)
        result = [-max_heap[0][0]]
        #print(max_heap)
        for i in range(k, len(nums)):
            heapq.heappush(max_heap,(-nums[i],i))
            #print(max_heap,i-k)
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            #print(max_heap)
            result.append(-max_heap[0][0]) 
        return result