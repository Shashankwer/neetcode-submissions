class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n_largest = heapq.nlargest(k, nums)
        return n_largest[-1]