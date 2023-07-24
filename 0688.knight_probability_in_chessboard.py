class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
        queue = defaultdict(list)
        queue[row, column] = 1
        p = 1
        for i in range(k):
            p = 0
            next_queue = defaultdict(int)
            for (r, c), prob in queue.items():
                for r_step, c_step in moves:
                    if 0 <= (nr := r + r_step) < n and 0 <= (nc := c + c_step) < n:
                        next_queue[nr, nc] += prob / 8
                        p += prob / 8
            queue = next_queue
        return p
