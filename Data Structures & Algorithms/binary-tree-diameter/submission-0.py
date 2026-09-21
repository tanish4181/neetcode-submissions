class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def rec(root):
            nonlocal result

            if not root:
                return 0

            left = rec(root.left)
            right = rec(root.right)

            result = max(result, left + right)

            return 1 + max(left, right)

        rec(root)
        return result