from queue import PriorityQueue


class Solution:
    def calculate_mst(self, edges, n, forced_edge=None):
        graph = defaultdict(list)
        visited = set()
        heap = PriorityQueue()
        res = 0
        for i, edge in enumerate(edges):
            graph[edge[0]].append((edge[2], edge[1]))
            graph[edge[1]].append((edge[2], edge[0]))
        if forced_edge == None:
            heap.put((0, 0))
        else:
            node1, node2, weight = edges[forced_edge]
            visited.update((node1, node2))
            res += weight
            for cost, node in graph[node1]:
                heap.put((cost, node))
            for cost, node in graph[node2]:
                heap.put((cost, node))
        while not heap.empty():
            cost, node = heap.get()
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for neig_cost, neig_node in graph[node]:
                if neig_node not in visited:
                    heap.put((neig_cost, neig_node))
        return float("inf") if len(visited) != n else res

    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        min_weight = self.calculate_mst(edges, n)
        print(min_weight)
        res = [[], []]
        for i in range(len(edges)):
            if self.calculate_mst(edges[:i] + edges[i + 1 :], n) > min_weight:
                res[0].append(i)
        for i in range(len(edges)):
            if i not in res[0]:
                if self.calculate_mst(edges, n, i) == min_weight:
                    res[1].append(i)
        return res
