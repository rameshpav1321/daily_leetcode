class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev,curr=head,head.next
        while curr!=None:
            if curr.val==prev.val:
                prev.next=curr.next
                prev=prev
            else:
                prev=curr
            curr=curr.next
        return head