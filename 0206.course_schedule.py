class Solution:
    def dfs(self, node, graph, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True
        for adj_node in graph[node]:
            if not visited[adj_node] and self.dfs(adj_node, graph, visited, rec_stack):
                return True
            elif rec_stack[adj_node]:
                return True
        rec_stack[node] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for prereq in prerequisites:
            print(prereq)
            for i in range(1, len(prereq)):
                graph[prereq[i]].append(prereq[i - 1])
        visited = [False] * numCourses
        rec_stack = [False] * numCourses
        for i in range(numCourses):
            if not visited[i]:
                if self.dfs(i, graph, visited, rec_stack):
                    return False
        return True
