class MinStack:

    def __init__(self):
        self.min_val = float("inf")
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            self.stack.append(val-self.min_val)
            if val < self.min_val:
                self.min_val = val

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.min_val = self.min_val - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return self.min_val + top
        else:
            return self.min_val
        

    def getMin(self) -> int:
        return self.min_val
        
