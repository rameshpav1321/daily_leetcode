class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or head.next==None:
            return head
        stack=[]
        curr=head
        length=0
        while curr:
            stack.append(curr)
            curr=curr.next
            length+=1
        curr=head
        for i in range(length//2):
            node=stack.pop()
            node.next=curr.next
            curr.next=node
            curr=curr.next.next
        if length%2==0:
            node.next=None
        else:
             node.next=stack.pop()
             node.next.next=None