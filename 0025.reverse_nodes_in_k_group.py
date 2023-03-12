class Solution:
    def size(self,head):
        count=0
        curr=head
        while curr.next:
            count+=1
            curr=curr.next
        return count+1

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr_dummy=dummy
        size=self.size(head)
        curr=head
        while size>=k:
            count=0
            stack=[]
            while count<k:
                stack.append(ListNode(curr.val))
                curr=curr.next
                count+=1
            while stack:
                curr_dummy.next=stack.pop()
                curr_dummy=curr_dummy.next
            size-=k
        curr_dummy.next=curr
        return dummy.next
