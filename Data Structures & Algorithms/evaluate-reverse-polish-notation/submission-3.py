class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            match tok:
                case "+":
                    left = stack.pop()
                    right = stack.pop()
                    left = left + right
                    stack.append(left)
                case "-":
                    left = stack.pop()
                    right = stack.pop()
                    left = right - left
                    stack.append(left)
                case "*":
                    left = stack.pop()
                    right = stack.pop()
                    left = left * right
                    stack.append(left)
                case "/":
                    left = stack.pop()
                    right = stack.pop()
                    left = int(right /left)
                    stack.append(left)
                case _ :
                    stack.append(int(tok))
        return stack[0]
                    
