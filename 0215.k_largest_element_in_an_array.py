from queue import PriorityQueue


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = PriorityQueue()
        for num in nums:
            q.put(-num)
        i = 0
        while not q.empty():
            res = -q.get()
            i += 1
            if i == k:
                return res
