class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = nums1[:m]
        index, l, r = 0, 0, 0
        while l<m and r<n:
            if left[l] < nums2[r]:
                nums1[index] = left[l]
                l+=1
            else:
                nums1[index] = nums2[r]
                r+=1
            index+=1
        while l < m:
            nums1[index] = left[l]
            l+=1
            index+=1
        while r < n:
            nums1[index] = nums2[r]
            r+=1
            index+=1
