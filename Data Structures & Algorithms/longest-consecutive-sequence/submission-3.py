class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        result = 1
        current_sequence_length = 1
        for index in range(1, len(nums)):
            if nums[index] - nums[index-1] == 1:
                current_sequence_length += 1
                if current_sequence_length > result:
                    result+=1
            elif nums[index] - nums[index-1] == 0:
                pass
            else:
                current_sequence_length = 1
        return result
                