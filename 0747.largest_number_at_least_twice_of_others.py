class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] == max_num:
                res = i
                continue
            if not max_num >= 2 * nums[i]:
                return -1
        return res
