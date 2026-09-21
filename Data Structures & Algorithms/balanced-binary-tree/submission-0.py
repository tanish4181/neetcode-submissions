# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        is_balance = False
        def rec(root):
            if not root:
                return 0
            nonlocal is_balance
            left = rec(root.left)
            right = rec(root.right)
            is_balance = True if left==right or abs(left-right)==1 else False
            return 1 + max(left,right)
        rec(root)
        return is_balance
        