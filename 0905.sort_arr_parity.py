class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        i,j=0,len(nums)-1
        for num in nums:
            if i<=j:
                if num%2==0:
                    res[i]=num
                    i+=1
                else:
                    res[j]=num
                    j-=1
        return res