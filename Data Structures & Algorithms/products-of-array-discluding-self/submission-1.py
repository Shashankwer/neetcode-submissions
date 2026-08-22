class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        prev = [0 for _ in range(arr_len)]
        suf = [0 for _ in range(arr_len)]
        res = [0 for _ in range(arr_len)]
        prev[0] = 1
        suf[-1] = 1
        for index in range(1, arr_len):
            prev[index] = nums[index-1] * prev[index-1]
            suf[-1-index] = nums[-index] * suf[-index]
        for index in range(arr_len):
            res[index] = prev[index]*suf[index]
        suf = None
        prev = None
        return res