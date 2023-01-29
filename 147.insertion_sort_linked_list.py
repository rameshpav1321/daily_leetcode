def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node=ListNode(0,head)
        prev,curr=head,head.next
        while curr:
            if curr.val>prev.val:
                prev,curr=curr,curr.next
                continue
            tmp_node=dummy_node
            while curr.val>tmp_node.next.val:
                tmp_node=tmp_node.next
            prev.next=curr.next
            curr.next=tmp_node.next
            tmp_node.next=curr
            curr=prev.next
        return dummy_node.next