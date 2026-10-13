# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs recursive 
        if not p and not q: 
            return True     # empty trees are equal 
            
        if not p or not q: return False
        if p.val != q.val: return False 

        # and now we just need to check if left == right
        return (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right))