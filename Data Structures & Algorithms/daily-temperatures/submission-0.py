class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_arr = []
        result = [0]* len(temperatures)
        for index,temp in enumerate(temperatures):
            if len(temp_arr) > 0:
                print(temp_arr[-1][1], temp)
            if len(temp_arr) > 0 and temp_arr[-1][1] < temp:
                ind, t = temp_arr.pop()
                while t< temp:
                    result[ind] = index-ind
                    if len(temp_arr) > 0 and temp_arr[-1][1] < temp:
                        ind, t = temp_arr.pop()
                    else:
                        t = temp
            temp_arr.append((index, temp))
        while temp_arr:
            index, temp = temp_arr.pop()
            result[index] = 0
        return result
