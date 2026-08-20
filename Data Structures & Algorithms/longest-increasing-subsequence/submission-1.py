class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {len(nums): 0}
        def recurseLTS(index):
            if index in cache:
                return cache[index]
            cache[index] = 1
            for i in range(index+1, len(nums)):
                if nums[index] < nums[i]:
                    cache[index] = max(cache[index], 1+recurseLTS(i))

        for index in range(len(nums)-1, -1, -1):
            recurseLTS(index)
        return max(list(cache.values()))