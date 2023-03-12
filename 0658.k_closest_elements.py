from queue import PriorityQueue
class Solution:
    def findClosestElements(self, lst: List[int], k: int, x: int) -> List[int]:
        priority_q=PriorityQueue()
        for item in lst:
            priority_q.put((abs(item-x),item))
        res=[]
        while priority_q.empty()==False:
            curr=priority_q.get()
            if len(res)!=k:
                res.append(curr[1])
        return sorted(res)