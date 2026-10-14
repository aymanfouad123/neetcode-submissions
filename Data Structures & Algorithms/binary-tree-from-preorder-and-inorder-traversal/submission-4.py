# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder: n l r
        inorder: l n r 

        take the next root from preorder
        find its position in inorder to split left and right subtrees
        use index bounds instead of copying slices
        """
        preorder = deque(preorder)
        lookup = {val: i for i, val in enumerate(inorder)}

        def dfs(left, right):
            # no elements in this range: no subtree
            if left > right:
                return None

            # preorder value is subtrees root
            val = preorder.popleft()
            root = TreeNode(val)

            # everything before mid belongs to the left subtree
            # everything after mid belongs to the right subtree
            mid = lookup[val]

            # building left first to consume preorder in the correct order
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)












