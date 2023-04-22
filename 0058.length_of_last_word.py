class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1])
        res,count=0,0
        s+=' '
        for char in s:
            if char!=' ':
                count+=1
            else:
                if count>0:
                    res=count
                count=0
        return res