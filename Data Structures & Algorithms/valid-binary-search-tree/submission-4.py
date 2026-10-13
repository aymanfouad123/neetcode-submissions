# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursive dfs
        return self.valid(root, float("-inf"), float("inf"))

    # need helper function to pass in the ranges
    def valid(self, node, leftRange, rightRange):
        if not node: return True
        if not (leftRange < node.val < rightRange):
                return False
            
        return self.valid(node.left, leftRange, node.val) and self.valid(node.right, node.val, rightRange)
