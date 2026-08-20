class Solution:
    digit_map = {
        "1": [],
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"],
        "0": ["+"]
    }
    def combineDigits(self, digit_1: List[str], digit_2: List[str]):
        if len(digit_1) == 0:
            return digit_2
        if len(digit_2) == 0:
            return digit_1
        res = []
        for c1 in digit_1:
            for c2 in digit_2:
                res.append(c1+c2)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        index = 0
        res = []
        while index < len(digits):
            if index == 0:
                res = self.digit_map[digits[index]]
            else:
                res = self.combineDigits(res, self.digit_map[digits[index]])
            index += 1
        return res    
        