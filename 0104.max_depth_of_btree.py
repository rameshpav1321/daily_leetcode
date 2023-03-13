class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            left=self.maxDepth(root.left)
            right=self.maxDepth(root.right)
            return max(left,right)+1
        return 0