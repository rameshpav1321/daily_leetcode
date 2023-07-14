class Solution:
    def dfs(self, node, graph, visited, rec_stack):
        print(node)
        visited[node] = True
        rec_stack[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node] and self.dfs(adj_node, graph, visited, rec_stack):
                return True
            elif rec_stack[adj_node]:
                return True
        rec_stack[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [False] * len(graph)
        rec_stack = [False] * len(graph)
        safe_nodes = []
        for node in range(len(graph)):
            self.dfs(node, graph, visited, rec_stack)
        for node in range(len(graph)):
            if not rec_stack[node]:
                safe_nodes.append(node)
        return safe_nodes
