class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return 
        if head.next==None:
            return head
        prev,curr=head,head.next
        while prev and curr:
            prev.val,curr.val=curr.val,prev.val
            if curr.next and curr.next.next:
                prev=curr.next
                curr=prev.next
            else:
                break
        return head