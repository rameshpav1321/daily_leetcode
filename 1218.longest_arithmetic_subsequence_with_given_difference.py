class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        res = 1
        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            res = max(res, dp[num])
        return res
