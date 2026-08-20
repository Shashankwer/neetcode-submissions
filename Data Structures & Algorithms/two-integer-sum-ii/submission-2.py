class Solution:
    def find_num(self, numbers, num):
        print(numbers, num)
        low = 0
        high = len(numbers) - 1
        mid = (high+low)//2
        while low <= high:
            if num == numbers[mid]:
                return mid+1
            elif num < numbers[mid]:
                high = mid - 1
            elif num > numbers[mid]:
                low = mid + 1
            mid = (high + low)//2
            
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(numbers)-1):
            index =  self.find_num(numbers[i+1:], target - numbers[i])
            if index!=-1:
                result.extend([i+1, i+index+1])
        return result