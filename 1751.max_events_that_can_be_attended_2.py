class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [start for start, end, val in events]
        dp = [[-1] * len(events) for i in range(k + 1)]

        def dfs(curr_ind, count):
            if count == 0 or curr_ind == len(events):
                return 0
            if dp[count][curr_ind] != -1:
                return dp[count][curr_ind]
            next_ind = bisect_right(starts, events[curr_ind][1])
            dp[count][curr_ind] = max(
                events[curr_ind][2] + dfs(next_ind, count - 1), dfs(curr_ind + 1, count)
            )
            return dp[count][curr_ind]

        return dfs(0, k)
