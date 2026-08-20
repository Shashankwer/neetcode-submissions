class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        partition_sum = total_sum // 2
        len_nums = len(nums)
        def isSolution(arr, index):
            sum_arr = sum(arr)
            if sum_arr == partition_sum:
                return True
            if sum_arr > partition_sum:
                return False
            if index>=len(nums):
                return False
            return  isSolution(arr+[nums[index]], index+1) or isSolution(arr, index+1)
        return  isSolution([], 0)           
