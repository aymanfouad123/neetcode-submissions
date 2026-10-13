# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative soln - not having to process whole tree
        stack = []
        curr = root
        n = 0

        while curr or stack:
            # first: go to the furthest left node till null
            while curr:
                stack.append(curr)
                curr = curr.left
            # when exiting we've exhausted all left nodes
            
            curr = stack.pop()  # processing last added ele

            # since we are processing this node 
            n += 1 
            if n == k: 
                return curr.val

            # now we need to go through right 
            curr = curr.right
