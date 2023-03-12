class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_lst=collections.defaultdict(list)
        for u,v,w in times:
            adj_lst[u].append((v,w))
        min_heap=[(0,k)]
        visited=set()
        res=0
        # djikstras
        while min_heap:
            time,node=heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            res=max(res,time)
            for nei_node,nei_time in adj_lst[node]:
                if nei_node not in visited:
                    heapq.heappush(min_heap,(time+nei_time,nei_node))
        return res if len(visited)==n else -1
