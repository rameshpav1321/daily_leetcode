class Solution:
    def dp(self, i, j, m, n, obstacleGrid, memo):
        if i > m or j > n or obstacleGrid[i][j] == 1:
            return 0
        if i == m and j == n:
            return 1
        if (i, j) not in memo:
            memo[(i, j)] = self.dp(i + 1, j, m, n, obstacleGrid, memo) + self.dp(
                i, j + 1, m, n, obstacleGrid, memo
            )
        return memo[(i, j)]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1
        memo = {}
        return self.dp(0, 0, m, n, obstacleGrid, memo)
