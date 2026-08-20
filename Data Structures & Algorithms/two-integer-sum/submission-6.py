class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_pos = {}
        for index, val in enumerate(nums):
            if val not in index_pos:
                index_pos[val] = [index]
            else:
                index_pos[val].append(index)
        for val in nums:
            difference = target - val
            if difference in index_pos and val != difference:
                return [index_pos[val][0], index_pos[difference][0]]
            elif difference in index_pos and val == difference and len(index_pos[difference]) > 1:
                return index_pos[difference][:2]
        return -1, -1