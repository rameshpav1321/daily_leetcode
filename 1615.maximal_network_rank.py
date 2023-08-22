class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        res = 0
        graph = defaultdict(list)
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                count = 0
                visited_paths = set()
                for adj_node in graph[node1]:
                    if (node1, adj_node) not in visited_paths:
                        visited_paths.add((node1, adj_node))
                        visited_paths.add((adj_node, node1))
                        count += 1
                for adj_node in graph[node2]:
                    if (node2, adj_node) not in visited_paths:
                        visited_paths.add((node2, adj_node))
                        visited_paths.add((adj_node, node2))
                        count += 1
                res = max(res, count)
        return res
