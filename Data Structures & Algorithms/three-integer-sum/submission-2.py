class Solution:
    def find_three_sum(self, nums, target, i, j):
        results = []
        while i < j:
            if (nums[i] + nums[j]) == -target:
                results.append([target,nums[i],nums[j]])
                i+=1
            elif (nums[i] + nums[j]) < -target:
                i += 1
            else:
                j -=1
        return results
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        nums_len = len(nums)
        for index in range(0, len(nums)-2):
            temp_result = self.find_three_sum(nums,nums[index],index+1,  nums_len-1)
            if len(temp_result)!=0:
                for tr in temp_result:
                    if tr not in results:
                        results.append(tr)
        return results