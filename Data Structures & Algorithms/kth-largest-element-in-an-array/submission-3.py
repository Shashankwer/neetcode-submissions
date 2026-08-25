class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = []
        for num in nums:
            #print(temp)
            heapq.heappush(temp, num)
            if len(temp) > k:
                heapq.heappop(temp)
        #print(temp)
        return temp[0]
