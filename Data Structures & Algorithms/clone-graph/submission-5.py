"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None 

        oldToNew = {}

        def dfs(curr):
            # first check if it is visited to reuse copy
            if curr in oldToNew:
                return oldToNew[curr]
            
            copy = Node(curr.val)
            oldToNew[curr] = copy 

            for neighbor in curr.neighbors: 
                neighborCopy = dfs(neighbor)
                copy.neighbors.append(neighborCopy)

            return copy
        
        return dfs(node) 