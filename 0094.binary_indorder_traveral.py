class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res,stack=[],[]
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            res.append(root.val)
            root=root.right
        return res