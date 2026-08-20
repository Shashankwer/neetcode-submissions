class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        inv_dict = {}
        for key, value in count.items():
            if value in inv_dict:
                inv_dict[value].append(key)
            else:
                inv_dict[value] = [key]
        result = []
        for value in sorted(inv_dict.keys(), reverse=True):
            print(inv_dict[value],k)
            for v in inv_dict[value]:
                result.append(v)
                k-=1
                if k <1:
                    break
            if k<1:
                break
        return result