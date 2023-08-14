class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_arr = []
        suffix_arr = []
        prefix_sum, suffix_sum = 0, 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            suffix_sum += nums[~i]
            prefix_arr.append(prefix_sum)
            suffix_arr.append(suffix_sum)
        suffix_arr.reverse()
        for i in range(len(nums)):
            if prefix_arr[i] == suffix_arr[i]:
                return i
        return -1
