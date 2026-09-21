# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def rec(root):
            if not root:
                return None
            left = rec(root.right)
            right = rec(root.left)
            root.left = right
            root.right = left
            return root
            
        
        return rec(root)
         