class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for row in matrix:
            res += row
        res.sort()
        return res[k - 1]
