class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        index = 1
        while index in nums_set:
            index += 1
        return index