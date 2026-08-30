class Arithmitic:
    def __init__(self):
        self.nums = []
        # self.armap = {"+": self.add, '-': self.sub, '*': self.mult, '/': self.div}
    
    def operation(self, tok):
        if tok == '+':
            # self.add()
            n2 = self.nums.pop()
            n1 = self.nums.pop()
            self.nums.append(n1 + n2)
        elif tok == '-':
            # self.sub()
            n2 = self.nums.pop()
            n1 = self.nums.pop()
            self.nums.append(n1 - n2)
        elif tok == '*':
            # self.mult()
            n2 = self.nums.pop()
            n1 = self.nums.pop()
            self.nums.append(n1 * n2)
        elif tok == '/':
            # self.div()
            n2 = self.nums.pop()
            n1 = self.nums.pop()
            self.nums.append(int(n1 / n2))
        else:
            self.nums.append(int(tok))

    # def add(self):
    #     n2 = self.nums.pop()
    #     n1 = self.nums.pop()
    #     self.nums.append(n1 + n2)

    # def sub(self):
    #     n2 = self.nums.pop()
    #     n1 = self.nums.pop()
    #     self.nums.append(n1 - n2)


    # def mult(self):
    #     n2 = self.nums.pop()
    #     n1 = self.nums.pop()
    #     self.nums.append(n1 * n2)


    # def div(self): 
    #     n2 = self.nums.pop()
    #     n1 = self.nums.pop()
    #     self.nums.append(int(n1 / n2))

    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        m = Arithmitic()
        for n in tokens:
            m.operation(n)
        return m.nums[-1]
        
        