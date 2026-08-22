class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                seq_len = 1
                while current + 1 in num_set:
                    current += 1
                    seq_len += 1
                result = max(seq_len, result)
        return result