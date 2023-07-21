class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                res += 1
                if intervals[i][1] < prev[1]:
                    prev = intervals[i]
            else:
                prev = intervals[i]
        return res
