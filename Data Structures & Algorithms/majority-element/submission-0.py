class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_size = int(len(nums)/2)
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
            if num_map[num] > majority_size:
                return num

