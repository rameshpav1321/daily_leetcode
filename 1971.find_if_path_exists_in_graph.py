# bfs
from queue import Queue
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_lst=[[] for i in range(n)]
        for edge in edges:
            adj_lst[edge[0]].append(edge[1])
            adj_lst[edge[1]].append(edge[0])
        visited={source}
        q=Queue()
        q.put(source)
        while q.empty()==False:
            curr=q.get()
            if curr==destination:
                return True
            for node in adj_lst[curr]:
                if node not in visited:
                    q.put(node)
                    visited.add(node)
        return False

# dfs
class Solution:
    def dfs(self,adj_lst,src,dst,visited):
        print(src,dst)
        visited.add(src)
        if src==dst:
            return True
        for node in adj_lst[src]:
            if node not in visited:
                if self.dfs(adj_lst,node,dst,visited):
                    return True

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_lst=[[] for i in range(n)]
        for edge in edges:
            adj_lst[edge[0]].append(edge[1])
            adj_lst[edge[1]].append(edge[0])
        print(adj_lst)
        visited=set()
        return self.dfs(adj_lst,source,destination,visited)
       
        
