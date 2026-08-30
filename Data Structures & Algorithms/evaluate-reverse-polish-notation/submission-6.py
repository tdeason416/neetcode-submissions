class Arithmitic:
    def __init__(self):
        self.nums = []
        self.armap = {"+": self.add, '-': self.sub, '*': self.mult, '/': self.div}
    
    def operation(self, tok):
        if tok not in self.armap:
            self.nums.append(int(tok))
        else:
            self.armap[tok]()

    def add(self):
        n2 = self.nums.pop()
        n1 = self.nums.pop()
        # print(f"add {n1} to {n2}")
        self.nums.append(n1 + n2)

    def sub(self):
        n2 = self.nums.pop()
        n1 = self.nums.pop()
        # print(f"sub {n2} from {n1}")
        self.nums.append(n1 - n2)


    def mult(self):
        n2 = self.nums.pop()
        n1 = self.nums.pop()
        # print(f"mult {n1} by {n2}")
        self.nums.append(n1 * n2)


    def div(self): 
        n2 = self.nums.pop()
        n1 = self.nums.pop()
        # print(f"div {n1} by {n2}")
        self.nums.append(int(n1 / n2))

    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        m = Arithmitic()
        for n in tokens:
            m.operation(n)
        return m.nums[-1]
        
        