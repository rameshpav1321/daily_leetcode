from queue import Queue


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(mat[0]) for _ in range(len(mat))]
        q = Queue()
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.put((i, j, 0))
                    visited.add((i, j))
        while not q.empty():
            i, j, val = q.get()
            for new_i, new_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (
                    (new_i, new_j) not in visited
                    and 0 <= new_i < len(mat)
                    and 0 <= new_j < len(mat[0])
                ):
                    visited.add((new_i, new_j))
                    q.put((new_i, new_j, val + 1))
                    res[new_i][new_j] = val + 1
        return res
