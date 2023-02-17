class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
       res=[]
       stack=[]
       i=1
       while len(stack)<len(target) and i<=n:
            if i in set(target):
                res.append('Push')
                stack.append(i)
            else:
                res.append('Push')
                res.append('Pop')
            i+=1
       return res