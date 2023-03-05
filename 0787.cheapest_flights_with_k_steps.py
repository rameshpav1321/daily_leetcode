from queue import PriorityQueue
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_lst=[[] for i in range(n)]
        for edge in flights:
            adj_lst[edge[0]].append((edge[1],edge[2]))
        dist=[float('inf')]*len(adj_lst)
        dist[src]=0
        q=PriorityQueue()
        q.put((0,src,0))
        while q.empty()==False:
            stops,curr_node,price=q.get()
            if stops>k:
                continue
            for adj_node,adj_node_price in adj_lst[curr_node]:
                if dist[adj_node]>dist[curr_node]+adj_node_price:
                    dist[adj_node]=price+adj_node_price
                    q.put((stops+1,adj_node,dist[adj_node]))
        return -1 if dist[dst]==float('inf') else dist[dst]