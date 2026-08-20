class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []
        index = 0
        for _ in range(len(nums)):
            if nums[index] != val:
                index += 1
            else:
                nums.pop(index)
        return len(nums)