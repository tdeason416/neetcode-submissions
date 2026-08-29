"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copy_nodes = {node: Node(node.val)}
        self.createNeighbors(node, copy_nodes)   # call once, no loop over node.neighbors
        return copy_nodes[node]

    def createNeighbors(self, o_node, copy_nodes):
        for n in o_node.neighbors:
            if n not in copy_nodes:
                copy_nodes[n] = Node(n.val)
                self.createNeighbors(n, copy_nodes)
            copy_nodes[o_node].neighbors.append(copy_nodes[n])
                
            

        