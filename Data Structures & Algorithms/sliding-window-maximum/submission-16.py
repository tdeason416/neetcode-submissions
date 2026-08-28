class Node:
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val
        self.morethan = None


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxNode = Node(0, nums[0])
        output = []
        if k == 1:
            output.append(maxNode.val)
        for idx in range(1, len(nums)):
            newNode = Node(idx, nums[idx])
            if newNode.val > maxNode.val:
                newNode.morethan = maxNode
                maxNode = newNode
            else:
                compNode = maxNode
                # while True:
                for _ in range(10):
                    nextComp = compNode.morethan
                    if not nextComp:
                        compNode.morethan = newNode
                        break
                    elif newNode.val >= nextComp.val:
                        newNode.morethan = nextComp
                        compNode.morethan = newNode
                        break
                    compNode = compNode.morethan
            if idx >= k - 1:
                while maxNode.idx <= idx - k:
                    maxNode = maxNode.morethan
            if idx >= k-1:
                output.append(maxNode.val)
        return output
        



        