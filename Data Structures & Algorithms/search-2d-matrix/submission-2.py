class Solution:
    def binSearch(self, nums, target):
        l, r = 0, len(nums)-1
        m = (l+r)//2
        while l<=r:
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m-1
            elif nums[m]<target:
                l = m+1
            m = (l+r)//2
        return nums[m]==target

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if target <=m[-1]:
                return self.binSearch(m, target)
        return False