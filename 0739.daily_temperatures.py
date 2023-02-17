class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for index,temp in enumerate(temperatures):
            while stack and temp>stack[-1][1]:
                prev_index,prev_temp=stack.pop()
                res[prev_index]=index-prev_index
            stack.append([index,temp])
        return res