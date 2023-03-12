class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # prefix, suffix, max_so_far = 0, 0, float('-inf')
        # for i in range(len(nums)):
        #     prefix = (prefix or 1) * nums[i]
        #     suffix = (suffix or 1) * nums[~i]
        #     max_so_far = max(max_so_far, prefix, suffix)
        # return max_so_far
        res=max(nums)
        curr_min=curr_max=1
        for num in nums:
            temp=curr_max*num
            curr_max=max(curr_max*num,curr_min*num,num)
            curr_min=min(temp,curr_min*num,num)
            res=max(res,curr_max)
        return res