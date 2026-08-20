class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for num in nums:
            if num is not None:
                for result in results:
                    if num not in result:
                        results.append(result+[num])
        return results    