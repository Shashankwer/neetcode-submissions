class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) < 3:
            return []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val > 0:
                    right -= 1
                elif val < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res