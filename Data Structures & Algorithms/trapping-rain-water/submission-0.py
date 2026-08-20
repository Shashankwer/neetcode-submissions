class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_maximum = -1
        suffix_maximum = -1
        num_indexes = len(height)
        prefix_max = [0]*num_indexes
        suffix_max = [0]*num_indexes
        for index in range(num_indexes):
            if height[index]>prefix_maximum:
                prefix_maximum = height[index]
            if height[(num_indexes-index-1)]>suffix_maximum:
                suffix_maximum = height[(num_indexes-index-1)]
            prefix_max[index] = prefix_maximum
            suffix_max[num_indexes-index-1] = suffix_maximum
        area = 0
        for index in range(num_indexes):
            area += max(min(prefix_max[index], suffix_max[index]) - height[index],0)
        return area