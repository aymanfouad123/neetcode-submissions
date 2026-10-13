# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterative dfs - stack
        stack = [(p, q)]

        while stack:
            nodeP, nodeQ = stack.pop()
            # both are empty: they match
            if not nodeP and not nodeQ:
                continue
            if not nodeP or not nodeQ or nodeP.val != nodeQ.val: 
                return False 
            
            stack.append((nodeP.right, nodeQ.right))
            stack.append((nodeP.left, nodeQ.left))

        return True
