class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        res = []
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            if nums[i] != start:
                res.append(str(start) + "->" + str(nums[i]))
            else:
                res.append(str(start))
            i += 1
        return res
