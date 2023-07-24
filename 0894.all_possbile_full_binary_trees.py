# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
dp = {0: [], 1: [TreeNode()]}


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n in dp:
            return dp[n]
        res = []
        for i in range(n):
            left, right = self.allPossibleFBT(i), self.allPossibleFBT(n - i - 1)
            for node1 in left:
                for node2 in right:
                    res.append(TreeNode(0, node1, node2))
        dp[n] = res
        return res
