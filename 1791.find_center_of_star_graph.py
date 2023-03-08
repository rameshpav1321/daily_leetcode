class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj_lst=[[] for i in range(len(edges)+1)]
        for edge in edges:
            adj_lst[edge[0]-1].append(edge[1]-1)
            adj_lst[edge[1]-1].append(edge[0]-1)
        for i,lst in enumerate(adj_lst):
            if len(lst)==len(edges):
                return i+1
            
# alternate solution

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1]:
            return edges[0][0]
        return edges[0][1]