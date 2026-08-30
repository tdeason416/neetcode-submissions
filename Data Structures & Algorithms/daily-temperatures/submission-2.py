class TempNode:
    def __init__(self, temp, idx):
        self.t = temp
        self.i = idx
        self.right = None

class Solution:
    def traverse(self, n_new, n_old, output):
        if not n_old:
            return output
        if n_new.t > n_old.t:
            output[n_old.i] = n_new.i - n_old.i
            n_old = n_old.right
            return self.traverse(n_new, n_old, output)
        n_new.right = n_old
        return output

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        root = None
        for idx in range(len(temperatures)):
            output.append(0)
            node = TempNode(temperatures[idx], idx)
            output = self.traverse(node, root, output)
            root = node
        return output


            

        