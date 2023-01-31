class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2=list1,list2
        dummy=ListNode(0)
        curr_dummy=dummy
        while curr1 and curr2:
            if curr1.val<=curr2.val:
                curr_dummy.next=ListNode(curr1.val)
                curr_dummy=curr_dummy.next
                curr1=curr1.next
            else:
                curr_dummy.next=ListNode(curr2.val)
                curr_dummy=curr_dummy.next
                curr2=curr2.next
        if not curr1:
            curr_dummy.next=curr2
        else:
            curr_dummy.next=curr1
        return dummy.next