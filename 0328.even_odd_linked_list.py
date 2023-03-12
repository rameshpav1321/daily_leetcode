class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            odd_node=head
            even_node,even_head=head.next,head.next
            while even_node.next and even_node.next.next:
                    odd_node.next=even_node.next
                    odd_node=odd_node.next
                    even_node.next=odd_node.next
                    even_node=even_node.next
            if even_node.next:
                odd_node.next=even_node.next
                odd_node=odd_node.next
                even_node.next=None
            odd_node.next=even_head
        return head