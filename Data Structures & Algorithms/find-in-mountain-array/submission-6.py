class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 1, mountainArr.length()-2
        while l<=r:
            m = (l+r)//2
            left, middle, right = mountainArr.get(m-1),mountainArr.get(m), mountainArr.get(m+1)
            if left < middle < right:
                l = m+1
            elif left > middle > right:
                r = m-1
            else:
                break
        #print("pivot", m, middle)
        pivot = m
        l,r = 0, pivot-1
        while l <= r:
            m = (l+r)//2
            middle = mountainArr.get(m)
            #print(l,r,m,left, right,middle)
            if middle == target:
                return m
            elif middle > target:
                r = m-1
            else:
                l = m+1
        # search right side
        l = pivot
        r = mountainArr.length()-1      
        while l <= r:
            m = (l+r)//2
            middle = mountainArr.get(m)
            #print(l,r,m,left, right,middle)
            if middle == target:
                #print("here")
                return m
            elif middle > target:
                l = m+1
            else:
                r = m-1
        return -1
                 

        # find element in first half