class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        mid = (r + l)//2
        while r>l:
            print(nums[mid], l, r, mid)
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                r = mid -1
                mid = (r+l)//2
            else:
                l = mid+1
                mid = (r+l)//2
        if nums[l]==target:
            return l
        else:
            #print(l,r, mid)
            return -1