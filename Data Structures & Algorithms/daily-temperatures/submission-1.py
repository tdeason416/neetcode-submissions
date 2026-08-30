class TempNode:
    def __init__(self, temp, idx):
        self.t = temp
        self.i = idx
        # self.left = None
        self.right = None

class Solution:
    def traverse(self, n_new, n_old, output):
        if not n_old:
            return output
        if n_new.t > n_old.t:
            # print(n_new.i, n_old.i)
            output[n_old.i] = n_new.i - n_old.i
            n_old = n_old.right
            return self.traverse(n_new, n_old, output)
        n_new.right = n_old
        return output

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # root = TempNode(temperatures[0], 0)
        output = []
        root = None
        # for idx in range(1, len(temperatures)):
        for idx in range(len(temperatures)):
            output.append(0)
            # print('temp node:', temperatures[idx], idx)
            node = TempNode(temperatures[idx], idx)
            # if node.t > root.t:
            #     node.left = root
            # elif node.t < root.t:
            #     node.right = root
            output = self.traverse(node, root, output)
            root = node

        return output


            

        