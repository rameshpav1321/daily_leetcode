class Solution:
    def maxArea(self, nums: List[int]) -> int:
        res=[]
        low,high=0,len(nums)-1
        while low<high:
            res.append((high-low)*min(nums[low],nums[high]))
            if nums[low]<nums[high]:
                low+=1
            elif nums[low]>nums[high]:
                high-=1
            else:
                low+=1
                high-=1
        return max(res)