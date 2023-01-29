import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_lst = {new_list: [] for new_list in range(len(points))}
        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(len(points)):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj_lst[i].append([dist,j])
                adj_lst[j].append([dist,i])
        # prims
        res=0
        visited=set()
        min_heap=[[0,0]]
        while len(visited)<len(points):
            cost,node= heapq.heappop(min_heap)
            if node in visited:
                continue
            res+=cost
            visited.add(node)
            for nei_cost,nei in adj_lst[node]:
                if nei not in visited:
                    heapq.heappush(min_heap,[nei_cost,nei])
        return res    