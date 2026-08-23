class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) < 4:
            return []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    val = nums[i] + nums[j] + nums[left] + nums[right]
                    if val > target:
                        right -= 1
                    elif val < target:
                        left += 1
                    else:
                        if [nums[i],nums[j], nums[left], nums[right]] not in res:
                            res.append([nums[i],nums[j], nums[left], nums[right]])
                        left+=1
                        right-=1
                        #while nums[left] == nums[left-1] and left < right:
                        #    left += 1
        return res