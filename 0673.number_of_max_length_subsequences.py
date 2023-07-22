class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        maxLis, res = 0, 0
        for i in range(len(nums)):
            currMax, currCount = 1, 1
            for j in range(i):
                j_len, j_count = dp[j]
                if nums[j] < nums[i]:
                    if j_len + 1 > currMax:
                        currMax, currCount = j_len + 1, j_count
                    elif j_len + 1 == currMax:
                        currCount += j_count
            dp[i] = [currMax, currCount]
            if currMax > maxLis:
                maxLis, res = currMax, currCount
            elif currMax == maxLis:
                res += currCount
        return res
