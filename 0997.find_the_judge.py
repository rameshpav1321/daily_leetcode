class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj_lst=[[] for i in range(n)]
        for edge in trust:
            adj_lst[edge[1]-1].append(edge[0]-1)
        res=-1
        for i in range(len(adj_lst)):
            if len(adj_lst[i])==n-1:
                res=i+1
        for lst in adj_lst:
            if res-1 in lst:
                return -1
        return res