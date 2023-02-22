class Solution:
    def largest_histogram_area(self,heights):
        stack=[]
        res=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                res=max(res,height*(i-index))
                start=index
            stack.append((start,h))
        for i,h in stack:
            res=max(res,(len(heights)-i)*h)
        return res
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix[0]=[int(i) for i in matrix[0]]
        max_rect=self.largest_histogram_area(matrix[0])
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j])==1:
                    matrix[i][j]=1+matrix[i-1][j]
                else:
                    matrix[i][j]=0
            max_rect=max(max_rect,self.largest_histogram_area(matrix[i]))
        return max_rect