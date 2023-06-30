class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                count = 0
            else:
                count += 1
                max_count = max(max_count, count)
        return max_count
