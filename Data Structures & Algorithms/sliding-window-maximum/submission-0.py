class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        left = 0
        nums_len = len(nums)
        while (left + k) <= nums_len:
            results.append(max(nums[left:left+k]))
            left+=1
        return results
