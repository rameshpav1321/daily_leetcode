class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(root):
            if not root:
                return [0,True]
            left,right=traverse(root.left),traverse(root.right)
            is_balanced= left[1] and right[1] and abs(left[0]-right[0])<=1
            return [max(left[0],right[0])+1,is_balanced]
        return traverse(root)[1]