class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums_arr = len(nums)
        def calcSubset(index, arr):
            if index == nums_arr:
                res.add(tuple(arr))
                return
            arr.append(nums[index])
            calcSubset(index+1, arr)
            arr.pop()
            calcSubset(index+1, arr)
        nums.sort()
        calcSubset(0, [])
        return [list(s) for s in res]