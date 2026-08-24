class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for val in tokens:
            # print(result,val)
            match val:
                case "+":
                    val2 = result.pop()
                    val1 = result.pop()
                    result.append((val1+val2))
                case "*":
                    val2 = result.pop()
                    val1 = result.pop()
                    result.append((val1*val2))
                case "-":
                    val2 = result.pop()
                    val1 = result.pop()
                    result.append((val1-val2))
                case "/":
                    val2 = result.pop()
                    val1 = result.pop()
                    
                    result.append(int(val1/val2))
                case _:
                    result.append(int(val))
        return result[0]
