# O(n log n)
class Solution:
    def check_window_size(self, nums, size, target):
        curr_sum = sum(nums[:size])
        if curr_sum >= target:
            return True
        for i in range(size, len(nums)):
            curr_sum += nums[i] - nums[i - size]
            if curr_sum >= target:
                return True
        return False

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low, high = 1, len(nums)
        res = 0
        while low <= high:
            mid = high - (high - low) // 2
            if self.check_window_size(nums, mid, target):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res


# O(n)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")
        for r in range(len(nums)):
            print(r)
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if res == float("inf") else res
