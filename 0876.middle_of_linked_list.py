class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next==None:
                return head
            count=1
            curr_node=head
            while curr_node.next!=None:
                count+=1
                curr_node=curr_node.next
            i=0
            while i!=count//2:
                print(i)
                head=head.next
                i+=1
            return head       
        return