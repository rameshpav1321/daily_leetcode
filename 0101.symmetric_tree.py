# recursive
class Solution:
    def compare_tree(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val==right.val and self.compare_tree(left.left,right.right) and self.compare_tree(left.right,right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compare_tree(root.left,root.right)
    # iterative
    from queue import Queue
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q=Queue()
        if not root.left and not root.right:
            return True
        else:
            q.put(root.left)
            q.put(root.right)
        while q.empty()==False:
            left=q.get()
            right=q.get()
            if not left and not right:
                continue
            if (not left and right) or (not right and left):
                return False
            if left.val!=right.val:
                return False
            q.put(left.left)
            q.put(right.right)
            q.put(left.right)
            q.put(right.left)
        return True