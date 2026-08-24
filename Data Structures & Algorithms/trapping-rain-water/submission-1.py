class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0]*len(height)
        suffix_max = [0]*len(height)
        prefix_max[0] = height[0]
        suffix_max[-1] = height[-1]
        result = 0

        for index in range(1,len(height)):
            prefix_max[index] = max(prefix_max[index-1], height[index])
        for index in range(len(height)-2,-1,-1):
            suffix_max[index] = max(suffix_max[index+1], height[index])
        for index in range(len(height)):
            result += max(0, min(prefix_max[index],suffix_max[index])-height[index])
        return result