class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        temp_stack = []
        for i, h in enumerate(heights):
            start = i
            while temp_stack and temp_stack[-1][1]>h:
                index, height = temp_stack.pop()
                area = max(area, height*(i-index))
                start = index
            temp_stack.append((start, h)) 
        for i, h in temp_stack:
            area = max(area, h*(len(heights)-i))
        return area
        