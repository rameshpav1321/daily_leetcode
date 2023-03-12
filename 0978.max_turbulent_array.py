class Solution:
    def maxTurbulenceSize(self, lst: List[int]) -> int:
        prev_sign=0
        count=1
        res=1
        for i in range(1,len(lst)):
            if lst[i]<lst[i-1] and (prev_sign==1 or prev_sign==0):
                prev_sign=-1
                count+=1
                res=max(res,count)
            elif lst[i]>lst[i-1] and (prev_sign==-1 or prev_sign==0):
                prev_sign=1
                count+=1
                res=max(res,count)
            else:
                count=1 if lst[i]==lst[i-1] else 2
        return res