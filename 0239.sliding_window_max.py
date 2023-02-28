class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        r=0
        q=collections.deque()
        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if r-q[0]>=k:
                q.popleft()
            if r+1>=k:
                res.append(nums[q[0]])
            r+=1
        return res
    
# O(nlogn) solution
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap, answer = [], []
        for index, num in enumerate(nums):
            heapq.heappush(heap, [-num, index])                
            while heap and heap[0][1] <= index - k:
                heapq.heappop(heap)
            if index >= k - 1:
                answer.append(-heap[0][0])
        return answer