class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for subset in subsets:
            for num in nums:
                if num not in subset:
                    subset_copy = sorted(subset + [num])
                    if subset_copy not in subsets:
                        subsets.append(subset_copy)
        return subsets
            
        