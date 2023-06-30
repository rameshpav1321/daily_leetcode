class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum, max_normal, max_sum, min_sum, max_circular = (
            0,
            nums[0],
            0,
            0,
            nums[0],
        )
        for num in nums:
            max_sum = max(max_sum + num, num)
            max_normal = max(max_normal, max_sum)
            min_sum = min(min_sum + num, num)
            max_circular = min(max_circular, min_sum)
            total_sum += num
        return (
            max(max_normal, total_sum - max_circular) if max_normal > 0 else max_normal
        )
