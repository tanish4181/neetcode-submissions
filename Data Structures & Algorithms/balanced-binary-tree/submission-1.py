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
        is_balance = True
        def rec(root):
            nonlocal is_balance
            if not root :
                return 0
            left = rec(root.left)
            right = rec(root.right)
            is_balance = is_balance and (abs(left - right) <= 1)
            return 1 + max(left,right)
        rec(root)
        return is_balance
        