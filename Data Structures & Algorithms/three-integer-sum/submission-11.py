class Solution:
    def findTwoSum(self, target):
        #print(target)
        result = []
        l,r = 0, len(self.nums)-1
        while l < r:
            #print(target,l, r, self.nums[l], self.nums[r], self.nums[l] + self.nums[r])
            while l in self.seen:
                #print(f"{l} in {self.seen} {self.nums}")
                l+=1
            while r in self.seen:
                r-=1
            #print(target,l, r, self.nums[l], self.nums[r], self.nums[l] + self.nums[r])
            if l < r:
                s = self.nums[l] + self.nums[r]
                if s == target:
                    res = sorted([-target, self.nums[l], self.nums[r]])
                    if res not in self.result and res not in result:
                        result.append(res)
                    l+=1
                    r-=1
                elif s < target:
                    l+=1
                else:
                    r-=1
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.seen = set()
        self.nums = sorted(nums)
        for index, num in enumerate(self.nums):
            #print(f"finding {num}")
            self.seen.add(index)
            r = self.findTwoSum(-num)
            if r:
                self.result.extend(r)
                print(self.result)
                # self.seen.add(index1)
                # self.seen.add(index2)
            self.seen.remove(index)
        return self.result