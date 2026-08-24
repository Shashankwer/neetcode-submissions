class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {}
        for index,num in enumerate(nums):
            if num in num_map:
                #print(num_map[num], index)
                num_map[num] = num_map[num]-index
            else:
                num_map[num] = index
            if num_map[num]<0 and abs(num_map[num])<=k:
                return True
            else:
                num_map[num] = index
        #print(num_map)
        return False