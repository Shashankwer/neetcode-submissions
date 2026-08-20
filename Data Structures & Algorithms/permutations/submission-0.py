class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_len = len(nums)
        def permute(arr):
            if len(arr) == nums_len:
                if arr not in res:
                    res.append(arr)
            for num in nums:
                if num not in arr:
                    permute(arr+[num])
        permute([])
        return res