class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1, num2 = "", ""
        while l1 != None or l2 != None:
            num1 += str(l1.val) if l1 else ""
            num2 += str(l2.val) if l2 else ""
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        res_num = str(int(num1) + int(num2))
        dummy_node = ListNode()
        res = dummy_node
        for digit in res_num:
            dummy_node.next = ListNode(int(digit))
            dummy_node = dummy_node.next
        dummy_node.next = None
        return res.next
