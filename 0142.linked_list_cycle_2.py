class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_dict={}
        curr=head
        while curr and curr.next:
            if curr in my_dict:
                return my_dict[curr]
            my_dict[curr]=curr
            curr=curr.next
        