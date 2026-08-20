class Solution:
    def isValid(self, s: str) -> bool:
        valid_arr = []
        for char in s:
            if char in '([{':
                valid_arr.append(char)
            elif char in ')}]':
                if len(valid_arr)==0:
                    return False
                test_char = valid_arr.pop(-1)
                if char == ')' and test_char != '(':    
                    return False
                if char == '}' and test_char != '{':
                    return False
                if char == ']' and test_char != '[':
                    return False
        if len(valid_arr) == 0:
            return True
        else:
            return False