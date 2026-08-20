class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicated = False
        seen = []
        for num in nums:
            if num in seen:
                return True
            else:
                seen.append(num)
        return False