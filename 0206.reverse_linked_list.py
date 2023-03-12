# Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        stack=[]
        curr=head
        while curr.next!=None:
            stack.append(curr)
            curr=curr.next
        new_head=curr
        for i in range(len(stack)):
            curr.next=stack.pop()
            curr=curr.next
        curr.next=None
        return new_head
# Iterative using stack
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        prev,curr=None,head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

# Recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        rev=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return rev
