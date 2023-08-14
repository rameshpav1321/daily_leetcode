class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = max_sum = min_sum = 0
        for i in range(len(nums)):
            max_sum = max(max_sum + nums[i], nums[i])
            min_sum = min(min_sum + nums[i], nums[i])
            res = max(res, max_sum, -min_sum)
        return res
