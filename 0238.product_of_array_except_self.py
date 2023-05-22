class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1] * len(nums)
        postfix_arr = [1] * len(nums)
        prefix_val, postfix_val = 1, 1
        for i in range(len(nums)):
            prefix_val *= nums[i]
            postfix_val *= nums[~i]
            prefix_arr[i] = prefix_val
            postfix_arr[~i] = postfix_val
        res = [postfix_arr[1]]
        for i in range(1, len(nums) - 1):
            res.append(prefix_arr[i - 1] * postfix_arr[i + 1])
        res.append(prefix_arr[-2])
        return res
