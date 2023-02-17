class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        smallest=nums[0]
        stack=[(nums[0],float('inf'))]
        for i in range(1,len(nums)):
            smallest=min(smallest,nums[i])
            while stack and stack[-1][0]<=nums[i]:
                stack.pop()
            if stack and nums[i]>stack[-1][1]:
                return True
            stack.append((nums[i],smallest))
        return False