class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearch(arr, target):
            l, r = 0,len(arr)
            mid = (l+r)//2
            while l < r:
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                mid = (l+r)//2
            if arr[l] == target:
                return True
            else:
                return False
        for arr in matrix:
            if target >= arr[0] and target <= arr[-1]:
                return binSearch(arr, target)
        return False

