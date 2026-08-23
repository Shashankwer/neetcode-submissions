class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_map = {}
        req_len = len(nums)//3
        result = set()
        for num in nums:
            num_map[num] = num_map.get(num,0)+1
            if num_map[num] > req_len:
                result.add(num)
        return list(result)