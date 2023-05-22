class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= nums[-1]:
                res = min(res, nums[mid])
                high = mid - 1
            if nums[mid] > nums[-1]:
                low = mid + 1
        return res
