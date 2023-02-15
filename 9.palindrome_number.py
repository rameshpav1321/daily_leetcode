class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0
        # print(temp)
        while temp>0:
            print(temp)
            rev=rev*10+(temp%10)
            temp//=10
        return x==rev

# or

class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp=str(x)
        for i in range(len(tmp)//2):
            if tmp[i]!=tmp[~i]:
                return False
        return True