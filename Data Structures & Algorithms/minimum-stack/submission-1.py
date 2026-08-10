class MinStack:

    def __init__(self):
        self.minvals = [float('infinity')]
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minvals[-1]:
            self.minvals.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minvals[-1]:
            self.minvals.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minvals[-1]
        
