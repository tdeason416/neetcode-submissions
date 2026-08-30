class Arithmitic:
    def __init__(self):
        self.nums = []
        self.armap = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
    
    def operation(self, tok):
        if tok in self.armap:
            n2 = self.nums.pop()
            n1 = self.nums.pop()
            self.nums.append(self.armap[tok](n1,n2))
        else:
            self.nums.append(int(tok))

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        m = Arithmitic()
        for n in tokens:
            m.operation(n)
        return m.nums[-1]
        
        