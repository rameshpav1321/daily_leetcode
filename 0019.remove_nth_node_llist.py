class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        normal,delayed=head,dummy
        for i in range(n):
            normal=normal.next
        while normal!=None:
            normal=normal.next
            delayed=delayed.next
        delayed.next=delayed.next.next
        return dummy.next
       