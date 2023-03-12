from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_node=ListNode(0,None)
        res=dummy_node
        if len(lists):
            priority_q=PriorityQueue()
            for i in range(len(lists)):
                if lists[i]:
                    priority_q.put((lists[i].val,i,lists[i].next))
            while priority_q.empty()==False:
                curr=priority_q.get()
                res.next=ListNode(curr[0],None)
                res=res.next
                if curr[2]:
                    priority_q.put((curr[2].val,curr[1],curr[2].next))
        return dummy_node.next