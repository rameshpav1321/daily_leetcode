class Solution:
    def preorder(self,root,lst):
        if root:
            lst.append(root.val)
            self.preorder(root.left,lst)
            self.preorder(root.right,lst)
            return
        lst.append(None)
        return

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        lst1=[]
        lst2=[]
        self.preorder(p,lst1)
        self.preorder(q,lst2)
        return lst1==lst2
# alternate solution
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False