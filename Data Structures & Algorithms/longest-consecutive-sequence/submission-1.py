class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        result = 0
        nums = set(nums)
        current_seq = 0
        for i in range(min_num, max_num+1):
            print(i, nums,current_seq)
            if i in nums:
                current_seq +=1
            else:
                if current_seq > result:
                    result = current_seq
                current_seq = 0
                
        if current_seq > result:
            result = current_seq
        return result
