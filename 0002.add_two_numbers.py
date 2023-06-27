class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res_llist = ListNode()
        res_head = res_llist
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            curr_node_val = l1_val + l2_val + carry
            res_llist.next = ListNode(curr_node_val % 10)
            carry = curr_node_val // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res_llist = res_llist.next
        return res_head.next
