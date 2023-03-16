class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()
        for i in range(len(nums)-2):
            low,high=i+1,len(nums)-1
            while low<high:
                if nums[low]+nums[high]+nums[i]==0:
                    res.add((nums[i],nums[low],nums[high]))
                    low+=1
                    high-=1
                elif nums[low]+nums[high]+nums[i]<0:
                    low+=1
                else:
                    high-=1
        return res