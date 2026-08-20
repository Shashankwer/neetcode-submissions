class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water_retention = 0
        left =0
        right = len(heights)-1
        while left < right:
            retention = (right-left)*min(heights[right], heights[left])
            if retention > water_retention:
                water_retention = retention
            if heights[right]> heights[left]:
                left+=1
            else:
                right -=1
        return water_retention