class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        A = set()
        for num in nums:
            if num not in A:
                A.add(num)
            else:
                return True
        return False