class Solution:
    def mySqrt(self, x: int) -> int:
        low=1
        high=x
        ans=0
        while low<=high:
            mid=(low+high)//2
            if mid*mid<x:
                low=mid+1
                ans=mid
            elif mid*mid>x:
                high=mid-1
            else:
                return mid
        return ans