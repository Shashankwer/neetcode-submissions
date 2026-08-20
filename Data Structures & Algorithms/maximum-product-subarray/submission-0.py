class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        currMax,currMin = 1, 1
        for num in nums:
            temp = currMax * num
            currMax = max(currMax*num, currMin*num, num)
            currMin = min(temp, num*currMin, num)
            result = max(result, currMax)
        return result