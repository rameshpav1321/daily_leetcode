class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        i,j=0,1
        for num in nums:
            if num%2==0 and i<len(nums):
                res[i]=num
                i+=2
            if num%2!=0 and j<len(nums):
                res[j]=num
                j+=2
        return res