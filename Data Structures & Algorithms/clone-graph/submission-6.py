"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # slightly more intuitive approach 
        if not node: return None 

        root = node

        oldToNew = {}   # storing node, nei references

        stack = [root]
        visited = set()
        visited.add(root)

        # trying to map out original node and nei mappings
        while stack:
            node = stack.pop()
            oldToNew[node] = Node(val=node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
        
        # now we have a old_node -> new_node mapping, but no nei relations
        for oldNode, newNode in oldToNew.items():
            for nei in oldNode.neighbors:
                newNei = oldToNew[nei]  # get the node mapping for newNei
                newNode.neighbors.append(newNei)
        
        return oldToNew[root]   # new node ref are the vals

