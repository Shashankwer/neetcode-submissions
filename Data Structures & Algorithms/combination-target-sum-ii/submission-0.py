class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        def isSum(index, arr, curr_sum):
            if curr_sum > target:
                return None
            elif curr_sum == target:
                if arr not in res:
                    res.append(arr)
            elif index >= len(candidates):
                return None
            else:
                isSum(index+1, arr + [candidates[index]], curr_sum + candidates[index])
                isSum(index+1, arr, curr_sum)
        isSum(0,[], 0)
        return res