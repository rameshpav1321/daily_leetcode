import math


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev, curr = head, head.next
        while curr:
            gcd_node = ListNode(math.gcd(prev.val, curr.val))
            prev.next = gcd_node
            gcd_node.next = curr
            prev = curr
            curr = curr.next
        return head
