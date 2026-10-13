# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # dfs iterative - stack 
        if subRoot is None:
            return True
        if root is None:
            return False

        stack = [(root)]

        while stack:
            node = stack.pop()
            if node is None: continue

            if node.val == subRoot.val:
                subStack = [(node, subRoot)]
                matches = True

                while subStack:
                    nodeR, nodeSub = subStack.pop()
                    
                    if nodeR is None and nodeSub is None:
                        continue

                    # diff structure: reject candidate
                    if nodeR is None or nodeSub is None:
                        matches = False
                        break

                    # diff values: reject candidate
                    if nodeR.val != nodeSub.val:
                        matches = False
                        break

                    subStack.append((nodeR.right, nodeSub.right))
                    subStack.append((nodeR.left, nodeSub.left))

                if matches: return True
             
            # continue searching, after failed candidate
            stack.append(node.right)
            stack.append(node.left)
                
        return False