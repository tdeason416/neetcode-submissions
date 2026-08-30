class Arithmitic:
    def __init__(self):
        self.nums = []
        # self.armap = {"+": self.add, '-': self.sub, '*': self.mult, '/': self.div}
    
    def operation(self, tok):
        # if tok not in self.armap:
        #     self.nums.append(int(tok))
        # else:
            # self.armap[tok]()
        if tok == '+':
            self.add()
        elif tok == '-':
            self.sub()
        elif tok == '*':
            self.mult()
        elif tok == '/':
            self.div()
        else:
            self.nums.append(int(tok))

    def add(self):
        n2 = self.nums.pop()
        n1 = self.nums.pop()
        self.nums.append(n1 + n2)

    def sub(self):
        n2 = self.nums.pop()
        n1 = self.nums.pop()
        self.nums.append(n1 - n2)


    def mult(self):
        n2 = self.nums.pop()
        n1 = self.nums.pop()
        self.nums.append(n1 * n2)


    def div(self): 
        n2 = self.nums.pop()
        n1 = self.nums.pop()
        self.nums.append(int(n1 / n2))

    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        m = Arithmitic()
        for n in tokens:
            m.operation(n)
        return m.nums[-1]
        
        